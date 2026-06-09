AIRDROP_SIGNALS = [

    "FUNDING",

    "TESTNET",

    "NO_TOKEN",

    "QUESTS",

    "ACTIVE_GITHUB",

    "COMMUNITY_GROWTH",

    "MAINNET_USAGE",

    "PARTNERSHIPS"
]

class AirdropOpportunity:

    def init(
        self,
        project,
        ecosystem,
        funding,
        token_exists,
        testnet,
        score
    ):
        self.project = project
        self.ecosystem = ecosystem
        self.funding = funding
        self.token_exists = token_exists
        self.testnet = testnet
        self.score = score