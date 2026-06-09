JOB_SOURCES = [
    "Ethereum Foundation",
    "Optimism",
    "Arbitrum",
    "Polygon",
    "Solana",
    "Hedera",
    "Starknet",
    "Base",
    "Aave",
    "Uniswap"
]

def score_job(job):

    score = 50

    if job.remote:
        score += 20

    if job.category == "SECURITY":
        score += 15

    if job.category == "DEVREL":
        score += 10

    return score