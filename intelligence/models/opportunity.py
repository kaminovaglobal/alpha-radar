class Opportunity:

    def __init__(
        self,
        title,
        category,
        ecosystem,
        source,
        metadata
    ):
        self.title = title
        self.category = category
        self.ecosystem = ecosystem
        self.source = source
        self.metadata = metadata

        OPPORTUNITY_TYPES = [

    "AIRDROP",

    "JOB",

    "GRANT",

    "BOUNTY",

    "AMBASSADOR",

    "FELLOWSHIP",

    "HACKATHON",

    "SECURITY_REWARD"
]
        
def priority(score):

    if score >= 90:
        return "CRITICAL"

    if score >= 75:
        return "HIGH"

    if score >= 50:
        return "MEDIUM"

    return "LOW"