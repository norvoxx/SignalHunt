import requests
from bs4 import BeautifulSoup
from modules.Username.base import BaseSocialMedia

# TODO Voir API
class Pinterest(BaseSocialMedia):
    name = "pinterest"
    def __init__(self, username) -> None:
        super().__init__(username)
        self.username = username
        response = requests.get("https://www.pinterest.com/" + username)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, "html.parser")
        else:
            self.soup = None

    def exist(self) -> bool:
        if (self.soup.find("title").text == ""):
            return False
        else:
            return True

    def API(self):
        return {
            "exist" : self.exist(),
            "website": "pinterest",
            "tag": "plugins",
            "username": self.username,
            "avatar": "",
            "htmlUrl": ("https://www.pinterest.com/" + self.username)
        }