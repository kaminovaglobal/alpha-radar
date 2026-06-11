class User:

    def __init__(
        self,
        username,
        email,
        hashed_password,
        role="user",
        plan="free"
    ):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.role = role
        self.plan = plan