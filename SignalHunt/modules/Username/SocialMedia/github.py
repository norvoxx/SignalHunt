import requests
from bs4 import BeautifulSoup

class Github:
    def __init__(self, username:str)->None:
        self.username = username
        try:
            self.resp = requests.get(f'https://api.github.com/users/{username}')
        except:
            self.resp = None

    def exist(self)->bool:
        if self.resp:
            return True
        else:
            return False

    def getAvatar(self)->str:
        return self.resp.json()['avatar_url']

    def getHtmlUrl(self)->str:
        return  self.resp.json()['html_url']


    def dev(self)->None:
        if self.resp:
            print(self.resp.json())
