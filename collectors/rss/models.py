from unicodedata import category


class RSSItem:

    def __init__(
        self,
        title,
        link,
        published,
        category,
    ):
        self.title = title
        self.link = link
        self.published = published
        self.category = category