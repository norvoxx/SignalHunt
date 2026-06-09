import requests
from bs4 import BeautifulSoup
from modules.Username.base import BaseSocialMedia

class Instagram(BaseSocialMedia):
    name = "instagram"
    def __init__(self,username):
        super().__init__(username)

        self.username = username
        self.url = f"https://www.instagram.com/{username}"
        self.exist = False
        self.requestsData = None

        headers = {'User-Agent': 'Mozilla/5.0 MyRedditScraper/1.0'}
        response = requests.get(self.url, headers=headers)

        if response.status_code == 200:
            try:
                self.requestsData = BeautifulSoup(response.content, 'html.parser')
                self.item = self.requestsData.select_one("meta[property='og:description']")
                if self.item:
                    self.exist = True
            except:
                print(f'{username} is not a valid username')
                self.item = None
        else:
            print(f'{username} is not a valid username')
            self.item = None

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

    def API(self):
        return {
            "exist": self.exist,
            "website": "instagram",
            "tag": "plugins",
            "username": self.username,
            "avatar": self.getAvatar(),
            "htmlUrl": ('https://www.instagram.com/' + self.username)
        }