def rank(opportunities):

    return sorted(
        opportunities,
        key=lambda x: x.score,
        reverse=True
    )