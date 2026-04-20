import requests
from bs4 import BeautifulSoup

# TODO Voir API
def username(username):
    response = requests.get("https://www.pinterest.com/" + username)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        if (soup.find("title").text == ""):
            print(f'{username} is not a valid username')
            return False
        #print(soup.find("title").text)
        return True
    else:
        print('request failed')
        return False
