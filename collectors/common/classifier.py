ECOSYSTEMS = [

    "Ethereum",

    "Arbitrum",

    "Optimism",

    "Base",

    "Monad",

    "Initia",

    "Polygon",

    "Hedera",

    "Starknet",

    "Solana"
]

def classify(title):

    title = title.lower()

    if "grant" in title:
        return "GRANT"

    if "hackathon" in title:
        return "HACKATHON"

    if "job" in title:
        return "JOB"

    return "GENERAL"