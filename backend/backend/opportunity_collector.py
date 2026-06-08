projects = [
    {
        "name": "Monad",
        "category": "Airdrop"
    },
    {
        "name": "Initia",
        "category": "Testnet"
    },
    {
        "name": "Zora",
        "category": "Creator Economy"
    }
]

for project in projects:
    print(
        f"{project['name']} "
        f"({project['category']})"
    )