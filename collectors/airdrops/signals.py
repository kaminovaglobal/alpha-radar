def has_token(project):

    return project["token_exists"]


def has_testnet(project):

    return project["testnet"]


def funding_signal(project):

    return project["funding"] > 0