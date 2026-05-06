import requests
from datetime import datetime

class Reddit:
    def __init__(self, username):
        self.username = username
        headers = {'User-Agent': 'Mozilla/5.0 MyRedditScraper/1.0'}
        url = f"https://www.reddit.com/user/{username}/about.json"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            self.data = response.json()['data']
        else:
            self.data = None

    def getCreation(self):
        created_utc = self.data.get('created_utc')
        date_creation = datetime.fromtimestamp(created_utc).strftime('%Y-%m-%d %H:%M:%S')
        return date_creation

    def exist(self):
        if self.data:
            return True
        else:
            return False
