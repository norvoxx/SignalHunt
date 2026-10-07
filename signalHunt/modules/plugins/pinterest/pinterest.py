import requests
import json

from bs4 import BeautifulSoup
from modules.template import BaseSocialMedia
from utils.findkey import findKey
from utils.header import headerHTTP
class Pinterest(BaseSocialMedia):

    pluginWebsite = "pinterest"
    pluginName = "pinterest"
    pluginTags = ["social media", "scraping", "pinterest"]

    def __init__(self, username) -> None:
        super().__init__(username)

        self.username = username
        self.url = f"https://fr.pinterest.com/{username}/_profile/"

        self.exist = False
        self.requestsSuccessful = False
        self.requestsData = None
        self.data = None
        self.elapsed = 0.0

        try:
            response = requests.get(self.url, headers=headerHTTP(),timeout=5)
            self.elapsed = response.elapsed.total_seconds()

            if response.status_code == 200:
                self.requestsSuccessful = True
                soup = BeautifulSoup(response.content, "html.parser")
                if soup.find("title").text != "":
                    self.exist = True
                    self.data = json.loads(soup.find("script", {"id": "__PWS_INITIAL_PROPS__"}).string)

                elif response.status_code == 404:
                    self.requestsSuccessful = True
                    self.exist = False

        except requests.RequestException:
            self.requestsSuccessful = False


    def getImageProfil(self)->str | None:
        if self.exist:
            avatar_url = findKey(self.data, "image_xlarge_url")
            return avatar_url
        return None

    def UsernameSearch(self) -> dict:
        if not self.requestsSuccessful:

            return {
                "success": False,
                "message": "Error: bad request"
            }
        return {
            "success": True,
            "message": f"request to {self.pluginName} took {self.elapsed}s",
            "data": {
                "exist": self.exist,
                "website": self.pluginName,
                "tag": self.pluginTags,
                "username": self.username,
                "avatar": self.getImageProfil(),
                "htmlUrl":self.url
            }
        }