from weights import WEIGHTS


def score(signals):

    total = 0

    for key, value in signals.items():

        total += (
            value *
            WEIGHTS.get(key, 0)
        )

    return round(total)