

class ExportFormattingPipeline:
    """
    Prepares items for export by applying consistent column names and formatting values for CSV output.
    """

    def process_item(self, item, spider):
        return {
            "URL": item.get("url"),
            "Venue Name": item.get("name"),
            "Guest Capacity": item.get("guest_capacity"),
            "Contact": item.get("contact"),
            "Location": item.get("location"),
            "Highlights": ", ".join(item.get("highlights", [])) if item.get("highlights") else "",
        }
