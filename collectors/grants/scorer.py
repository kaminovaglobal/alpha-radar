def score_grant(grant):

    score = 50

    if grant["amount"] >= 100000:
        score += 30

    elif grant["amount"] >= 25000:
        score += 20

    elif grant["amount"] >= 10000:
        score += 10

    return score