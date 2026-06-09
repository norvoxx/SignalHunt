import requests
import json

from bs4 import BeautifulSoup
from modules.Username.base import BaseSocialMedia
from modules.Utils.findKey import findKey

class Pinterest(BaseSocialMedia):
    """
     A class to represent a Github username
     Attributes:
         username (str): The Github username
         url (str): The Github username
         exist (bool): Whether or not the username exists
         data (dict): A dictionary containing data about the username
    Methods:
        getImageProfil(str): Returns the avatar of the username
        API(str): Returns the username
    """
    name = "pinterest"

    def __init__(self, username) -> None:
        super().__init__(username)

        self.username = username
        self.url = f"https://fr.pinterest.com/{username}/_profile/"
        self.requestsData = None
        self.data = None

        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            if soup.find("title").text != "":
                self.exist = True
                self.data = json.loads(soup.find("script", {"id": "__PWS_INITIAL_PROPS__"}).string)

    def getImageProfil(self)->str | None:
        if self.exist:
            avatar_url = findKey(self.data, "image_xlarge_url")
            return avatar_url
        return None

    def API(self):
        return {
            "exist": self.exist,
            "website": "pinterest",
            "tag": "plugins",
            "username": self.username,
            "avatar": self.getImageProfil(),
            "htmlUrl": self.url
        }