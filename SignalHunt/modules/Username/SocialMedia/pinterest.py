import requests
from bs4 import BeautifulSoup

# TODO Voir API
class Pinterest:
    def __init__(self, username) -> None:
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

ca