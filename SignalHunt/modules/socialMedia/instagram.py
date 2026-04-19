import requests
from bs4 import BeautifulSoup

def username (username):
    response = requests.get('https://www.instagram.com/' + username)
    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            item = soup.select_one("meta[property='og:description']")
            name = item.find_previous_sibling().get("content").split("•")[0]
            #followers = item.get("content").split(",")[0]
            #following = item.get("content").split(",")[1].strip()
            print(f'{name}\n')
            return True
        except:
            print(f'{username} is not a valid username')
            return False
    else:
        print('request failed')
        return False