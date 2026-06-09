OPPORTUNITY_TYPES = [

    "AIRDROP",

    "TESTNET",

    "GRANT",

    "JOB",

    "BOUNTY",

    "AMBASSADOR",

    "HACKATHON",

    "GOVERNANCE",

    "SECURITY",

    "PARTNERSHIP",

    "FUNDING"
]

class Opportunity:

    def init(
        self,
        source,
        title,
        url,
        category,
        ecosystem
    ):
        self.source = source
        self.title = title
        self.url = url
        self.category = category
        self.ecosystem = ecosystem