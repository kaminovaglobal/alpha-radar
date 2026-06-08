from models import RSSItem


def parse_entry(entry):

    return RSSItem(
        title=entry.get("title"),
        link=entry.get("link"),
        published=entry.get(
            "published",
            "Unknown"
        )
    )