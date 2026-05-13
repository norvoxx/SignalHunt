import requests
from bs4 import BeautifulSoup
from modules.Username.base import BaseSocialMedia

class Instagram(BaseSocialMedia):
    name = "instagram"
    def __init__(self,username):
        super().__init__(username)
        self.username = username

        headers = {'User-Agent': 'Mozilla/5.0 MyRedditScraper/1.0'}
        response = requests.get('https://www.instagram.com/' + username, headers=headers)
        if response.status_code == 200:
            try:
                soup = BeautifulSoup(response.content, 'html.parser')
                self.item = soup.select_one("meta[property='og:description']")
                self.avatar_meta = soup.select_one("meta[property='og:image']")
            except:
                print(f'{username} is not a valid username')
                self.item = None
        else:
            print(f'{username} is not a valid username')
            self.item = None

    def exist(self):
        if self.item:
            return True
        else:
            return False

    def getFollowers(self):
        return self.item.get("content").split(",")[0]

    def getFollowing(self):
        return  self.item.get("content").split(",")[1].strip()

    def getAvatar(self):
        if self.avatar_meta:
            return self.avatar_meta.get("content")
        return "L'avatar n'a pas pu être récupéré"
    def API(self):
        return {
            "exist": self.exist(),
            "website": "instagram",
            "tag": "plugins",
            "username": self.username,
            "avatar": self.getAvatar(),
            "htmlUrl": ('https://www.instagram.com/' + self.username)
        }
    def dev(self):
        if self.item:
            print(self.item)