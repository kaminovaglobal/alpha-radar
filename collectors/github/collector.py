import requests

response = requests.get(
    "https://api.github.com/orgs/ethereum/repos"
)

repos = response.json()

for repo in repos[:5]:

    print(repo["name"])