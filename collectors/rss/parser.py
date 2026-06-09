from models import RSSItem

def categorize(title):

    title = title.lower()

    if "grant" in title:
        return "Grant"

    if "funding" in title:
        return "Funding"

    if "hack" in title:
        return "Security"

    return "General"

def parse_entry(entry):

    return RSSItem(
        title=entry.get("title"),
        link=entry.get("link"),
        published=entry.get(
            "published",
            "Unknown"
        ),
        category=entry.get("category")
    )