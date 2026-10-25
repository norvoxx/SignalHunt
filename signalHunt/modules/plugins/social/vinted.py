import requests
from bs4 import BeautifulSoup
from modules.template import BaseSocialMedia
from utils.header import headerHTTP

#TODO a modifier juste un debut
#? Pouvoir trouver des variation d'un speudo avec analyse d'image
#? Comparais la probabiliter que le compte appartien a la cible vias les image description langue amis

class Vinted(BaseSocialMedia):
    pluginWebsite = "vinted.com"
    pluginName = "vinted"
    pluginTags = ["social media","shop","scraping", "dev"]

    def __init__(self, username: str) -> None:
        super().__init__(username)
        self.url = f"https://www.vinted.fr/member/general/search?search_text={username}"
        self.exist = False
        self.requestsSuccessful = False
        self.elapsed = 0.0
        self.data = None

        self.getImageProfil = ""

        try:
            response = requests.get(self.url, headers=headerHTTP(), timeout=10)
            self.elapsed = response.elapsed.total_seconds()

            if response.status_code == 200:
                self.requestsSuccessful = True
                self.data =  BeautifulSoup(response.content,"html.parser")        

                div = self.data.find_all("div", {"class":"UserGrid-module-scss-module__DP7QeW__user-grid__item"})
                if (len(div)>0):
                    self.exist = True
                    self.getImageProfil = div[0].find("img")["src"]

            elif response.status_code == 404:
                self.requestsSuccessful = True
                self.exist = False

        except requests.RequestException:
            self.requestsSuccessful = False

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
                    "avatar": self.getImageProfil,
                    "htmlUrl":self.url
                }
        }
