import requests
from modules.template import BaseSocialMedia
from utils.header import headerHTTP

class TikTok(BaseSocialMedia):
    pluginWebsite = "Tiktok"
    pluginName = "Tiktok"
    pluginTags = ["social media", "scraping", "dev"]

    def __init__(self, username: str) -> None:
        super().__init__(username)
        self.url = f"https://www.tiktok.com/@{username}"
        self.exist = False
        self.requestsSuccessful = False
        self.elapsed = 0.0

        try:
            response = requests.get(self.url, headers=headerHTTP(), timeout=10)
            self.elapsed = response.elapsed.total_seconds()

            if response.status_code == 200:
                self.requestsSuccessful = True
                if 'statuscode":10221' in response.text or '"statusCode":10221' in response.text:
                    self.exist = False
                else :
                    self.exist = True
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
                    "avatar": "",
                    "htmlUrl": ""
                }
            }