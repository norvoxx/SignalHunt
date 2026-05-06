import requests
from bs4 import BeautifulSoup

class Instagram:
    def __init__(self,username):
        self.username = username

        headers = {'User-Agent': 'Mozilla/5.0 MyRedditScraper/1.0'}
        response = requests.get('https://www.instagram.com/' + username, headers=headers)
        if response.status_code == 200:
            try:
                soup = BeautifulSoup(response.content, 'html.parser')
                self.item = soup.select_one("meta[property='og:description']")
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

    def dev(self):
        if self.item:
            print(self.item)