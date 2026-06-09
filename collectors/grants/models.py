GRANT_SOURCES = [

    "Ethereum Foundation",

    "Optimism",

    "Arbitrum",

    "Polygon",

    "Solana",

    "Hedera",

    "Starknet",

    "Base",

    "Avalanche",

    "Near"
]

class GrantOpportunity:

    def __init__(
        self,
        program,
        ecosystem,
        category,
        amount,
        deadline,
        score
    ):
        self.program = program
        self.ecosystem = ecosystem
        self.category = category
        self.amount = amount
        self.deadline = deadline
        self.score = score