import requests
from modules.Username.base import BaseSocialMedia

class Github(BaseSocialMedia):
    """
    A class to represent a Github username

    Attributes:
        name (str): The name of the social media platform ("github").
        username (str): Github username.
        url (str): The GitHub API endpoint for the user.
        exist (bool): True if the user exists on GitHub, False otherwise.
        requestsData (dict | None): The raw JSON response from the GitHub API.

    Methods
        getAvatar(str) : Returns the avatar of the user
        getHtmlUrl(str) : Returns the html url of the user
        API(str) : Returns the user's infromation
    """

    name = "github"
    def __init__(self, username: str) -> None:

        super().__init__(username)

        self.username  = username
        self.url = f"https://api.github.com/users/{username}"
        self.exist = False
        self.requestsData = None

        try:
            response = requests.get(self.url, timeout=5)
            if response.status_code == 200:
                self.exist = True
                self.requestsData = response.json()

        except requests.RequestException:
            pass

    def getAvatar(self) -> str | None:
        if self.exist and self.requestsData:
            return self.requestsData.get("avatar_url", "")
        return None

    def getHtmlUrl(self) -> str | None:
        if self.exist and self.requestsData:
            return self.requestsData.get("html_url", "")
        return None

    def API(self):
        return {
            "exist": self.exist,
            "website": self.name,
            "tag": "plugins",
            "username": self.username,
            "avatar": self.getAvatar(),
            "htmlUrl": self.getHtmlUrl()
        }
