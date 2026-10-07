import requests
from bs4 import BeautifulSoup
from modules.template import BaseSocialMedia
from utils.header import headerHTTP


class Instagram(BaseSocialMedia):
    pluginWebsite = "instagram"
    pluginName = "instagram"
    pluginTags = ["social media", "scraping"]

    def __init__(self,username):
        super().__init__(username)
        
        self.username = username
        self.url = f"https://www.instagram.com/{username}"
        self.exist = False
        self.requestsSuccessful = False

        self.requestsData = None
        self.elapsed = 0.0
        try:
            headers = {'User-Agent': 'Mozilla/5.0 MyRedditScraper/1.0'}
            response = requests.get(self.url, headers=headers)
            self.elapsed = response.elapsed.total_seconds()
            
            if response.status_code == 200:
                try:
                    self.requestsSuccessful = True
                    self.requestsData = BeautifulSoup(response.content, 'html.parser')
                    self.item = self.requestsData.select_one("meta[property='og:description']")
                    if self.item: 
                        self.exist = True
                except:
                    print(f'{username} is not a valid username')
                    self.item = None
            
        except requests.RequestException:
            self.requestsSuccessful = False

    def getFollowers(self):
        if self.exist:
            return self.item.get("content").split(",")[0]
        return None

    def getFollowing(self):
        if self.exist:
            return  self.item.get("content").split(",")[1].strip()
        return None

    def getAvatar(self):
        if self.exist:
            return  self.requestsData.select_one("meta[property='og:image']").get("content")
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
                "avatar": self.getAvatar(),
                "htmlUrl":  'https://www.instagram.com/' + self.username
            }
        }