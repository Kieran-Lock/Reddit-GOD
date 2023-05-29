class RedditCredentials:
    def __init__(self, *, client_id: str, client_secret: str, user_agent: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.credentials = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "user_agent": self.user_agent
        }
