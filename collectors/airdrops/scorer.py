def score_project(project):

    score = 0

    if project["funding"] > 100:
        score += 30

    if project["testnet"]:
        score += 30

    if not project["token_exists"]:
        score += 40

    return score