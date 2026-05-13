import requests
from modules.Username.base import BaseSocialMedia

class TikTok(BaseSocialMedia):
    name = "TikTok"
    is_plugin = True

    def __init__(self, username: str) -> None:
        super().__init__(username)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
        }
        self.url = f"https://www.tiktok.com/@{username}"
        try:
            self.response = requests.get(self.url, headers=self.headers, timeout=10)
        except requests.RequestException:
            self.response = None

    def exist(self) -> bool:
        if self.response is None:
            return False
        if self.response.status_code == 404:
            return False
        if self.response.status_code == 200:
            if 'statuscode":10221' in self.response.text or '"statusCode":10221' in self.response.text:
                return False
            return True

        return False

    def API(self):
        return {
            "exist": self.exist(),
            "website": self.name,
            "tag": "plugins",
            "username": self.username,
            "avatar": "",
            "htmlUrl": self.url
        }