
class DuplicateHighlightRemovalPipeline:
    """
    Removes duplicate values from the 'highlights' field of scraped items.
    """

    def process_item(self, item, spider):
        highlights = item.get("highlights", [])
        seen = set()
        unique_highlights = []
        for h in highlights:
            if h not in seen:
                seen.add(h)
                unique_highlights.append(h)
        item["highlights"] = unique_highlights
        return item
