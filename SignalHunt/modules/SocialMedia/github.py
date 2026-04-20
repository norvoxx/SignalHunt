import requests
from bs4 import BeautifulSoup


def username(username:str)->bool:
    reponce = requests.get(f'https://api.github.com/users/{username}')
    try :
        print(reponce.json()["login"])
        return True
    except:
        print(f'{username} is not a valid username')
        return False