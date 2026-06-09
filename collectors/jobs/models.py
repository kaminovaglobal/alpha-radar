JOB_CATEGORIES = [

    "SECURITY",

    "DEVREL",

    "COMMUNITY",

    "GROWTH",

    "ENGINEERING",

    "CONTENT",

    "DESIGN",

    "RESEARCH",

    "OPERATIONS"
]
class Job:

    def init(
        self,
        title,
        company,
        location,
        remote,
        url,
        category
    ):
        self.title = title
        self.company = company
        self.location = location
        self.remote = remote
        self.url = url
        self.category = category