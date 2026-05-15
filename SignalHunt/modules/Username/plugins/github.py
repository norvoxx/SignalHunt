import requests
from modules.Username.base import BaseSocialMedia

class Github(BaseSocialMedia):
    name = "github"
    is_plugin = True
    def __init__(self, username: str) -> None:
        super().__init__(username)

        self.data = None
        self.status_code = None

        try:
            resp = requests.get(
                f"https://api.github.com/users/{username}",
                timeout=5
            )
            self.status_code = resp.status_code

            if resp.status_code == 200:
                self.data = resp.json()

        except requests.RequestException:
            self.status_code = None
            self.data = None

    def exist(self) -> bool:
        return self.status_code == 200

    def getAvatar(self) -> str:
        if self.exist():
            return self.data.get("avatar_url", "")
        return ""

    def getHtmlUrl(self) -> str:
        if self.exist():
            return self.data.get("html_url", "")
        return ""

    def API(self):
        return {
            "exist": self.exist(),
            "website": self.name,
            "tag": "plugins",
            "username": self.username,
            "avatar": self.getAvatar(),
            "htmlUrl": self.getHtmlUrl()
        }