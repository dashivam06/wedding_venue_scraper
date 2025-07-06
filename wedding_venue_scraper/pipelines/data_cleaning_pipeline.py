
class DataCleaningPipeline:
    """
    Cleans and normalizes scraped item fields.

    Trims strings, converts guest capacity to integer, 
    formats contact details, and removes empty highlight values.
    Ensures consistent data before storage or export.
    """


    def process_item(self, item, spider):

        contact = item.get("contact")
        if contact:
            item["contact"] = contact.replace("ext.", "ext ").strip()
        else:
            item["contact"] = None

        name = item.get("name")
        if name:
            item["name"] = name.strip()

        location = item.get("location")
        if location:
            item["location"] = location.strip()

        guest_capacity = item.get("guest_capacity")
        if guest_capacity:
            try:
                item["guest_capacity"] = int(guest_capacity)
            except (ValueError, TypeError):
                item["guest_capacity"] = None

        highlights = item.get("highlights")
        if highlights and isinstance(highlights, list):
            cleaned_highlights = []
            for h in highlights:
                cleaned = h.strip()
                if cleaned:
                    cleaned_highlights.append(cleaned)
            item["highlights"] = cleaned_highlights

        url = item.get("url")
        if url:
            item["url"] = url.strip()

        return item
