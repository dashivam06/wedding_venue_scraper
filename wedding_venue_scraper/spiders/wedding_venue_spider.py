import scrapy
import re

from ..items.weeding_venue_item import WeddingVenueItem


class WeddingVenueSpider(scrapy.Spider):
    """
    Spider for scraping wedding venue details from wedding-spot.com for selected regions.

    Extracts venue name, contact information, guest capacity, location, highlights, and paginates through results.
    """

    name = "wedding_venue_spider"
    allowed_domains = ["wedding-spot.com"]
    start_urls = [
        "https://www.wedding-spot.com/wedding-venues/?pr=new%20jersey&r=new%20jersey%3anorth%20jersey&r=new%20jersey%3aatlantic%20city&r=new%20jersey%3ajersey%20shore&r=new%20jersey%3asouth%20jersey&r=new%20jersey%3acentral%20jersey&r=new%20york%3along%20island&r=new%20york%3amanhattan&r=new%20york%3abrooklyn&r=pennsylvania%3aphiladelphia&sr=1"
    ]


    def parse(self, response):
        """
        Parses the listing page to extract venue detail links and follows pagination.
        """
        venue_links = response.css(".venueCard--wrapper a::attr(href)").getall()
        for link in venue_links:
            yield response.follow(link, callback=self.parse_detail)

        next_page_url = self.get_next_page_url(response.url, response)
        if next_page_url:
            yield scrapy.Request(next_page_url, callback=self.parse)



    def parse_detail(self, response):
        """
        Parses the venue detail page to extract structured information into an item.
        """
        guest_capacity = self.extract_guest_capacity(response)
        location = self.extract_location(response)
        highlights = self.extract_highlights(response)

        item = WeddingVenueItem(
            name=response.css(".SecondaryCTA--venueName::text").get(),
            url=response.url,
            contact=response.css(".SecondaryCTA--hidden::text").get(),
            guest_capacity=guest_capacity,
            location=location,
            highlights=highlights,
        )
        yield item


    def get_next_page_url(self, current_url, response):
        """
        Constructs the next page URL for pagination if available.

        Returns:
            str or None: Next page URL or None if no more pages.
        """

        if response.css('button[aria-label="Next Page"][disabled]'):
            return None

        current_page = int(re.search(r"page=(\d+)", current_url).group(1)) if "page=" in current_url else 1
        next_page = current_page + 1

        if "page=" in current_url:
            return re.sub(r"page=\d+", f"page={next_page}", current_url)
        else:
            separator = "&" if "?" in current_url else "?"
            return f"{current_url}{separator}page={next_page}"


    def extract_guest_capacity(self, response):

        text = response.css(
            '.icon-hb-nx-users+ .VenuePage--detail-text-container .VenuePage--detail-description::text'
        ).get()
        match = re.search(r"Accommodates up to (\d+)", text or "")
        return match.group(1) if match else None



    def extract_location(self, response):
        
        parts = response.css(
            '.icon-hb-nx-location-pin-32+ .VenuePage--detail-text-container .VenuePage--detail-description *::text'
        ).getall()
        return " ".join(part.strip() for part in parts if part.strip())
    


    def extract_highlights(self, response):
        return response.css(
            ".Panel--className .VenueHighlights--className .VenueHighlights--highlight .VenueHighlights--label::text"
        ).getall()


   