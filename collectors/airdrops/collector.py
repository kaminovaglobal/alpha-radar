from scorer import score_project

for project in projects:

    score = score_project(project)

    print(
        project["project"],
        score
    )

projects = [

    {
        "project": "Monad",
        "ecosystem": "Monad",
        "funding": 225,
        "token_exists": False,
        "testnet": True
    },

    {
        "project": "Initia",
        "ecosystem": "Initia",
        "funding": 25,
        "token_exists": False,
        "testnet": True
    }
]