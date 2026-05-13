import requests
from datetime import datetime
from modules.Username.base import BaseSocialMedia

class Reddit(BaseSocialMedia):
    name = "reddit"
    def __init__(self, username):
        super().__init__(username)

        self.username = username
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) MyProject/1.0'}
        url = f"https://www.reddit.com/user/{username}/about.json"

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                self.data = response.json()['data']
            else:
                self.data = None
        except Exception:
            self.data = None

    def get_avatar(self):
        if self.data and 'icon_img' in self.data:
            avatar_url = self.data.get('icon_img')
            return avatar_url.split('?')[0] if avatar_url else ""
        return ""

    def getCreation(self):
        if not self.data: return None
        created_utc = self.data.get('created_utc')
        return datetime.fromtimestamp(created_utc).strftime('%Y-%m-%d %H:%M:%S')

    def exist(self):
        return self.data is not None

    def API(self):
        return {
            "exist": self.exist(),
            "website": "reddit",
            "tag": "plugins",
            "username": self.username,
            "avatar": self.get_avatar(),  # Appel de la nouvelle méthode
            "htmlUrl": f"https://www.reddit.com/user/{self.username}"  # Correction Pinterest -> Reddit
        }