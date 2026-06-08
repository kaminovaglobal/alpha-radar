import feedparser

from feeds import RSS_FEEDS
from parser import parse_entry


all_items = []

for url in RSS_FEEDS:

    feed = feedparser.parse(url)

    for entry in feed.entries:

        item = parse_entry(entry)

        all_items.append(item)


print(
    f"Collected {len(all_items)} items"
)