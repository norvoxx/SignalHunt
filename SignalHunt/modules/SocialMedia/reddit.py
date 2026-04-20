import requests
from datetime import datetime

def username(username):
    headers = {'User-Agent': 'Mozilla/5.0 MyRedditScraper/1.0'}
    url = f"https://www.reddit.com/user/{username}/about.json"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        created_utc = data.get('created_utc')
        date_creation = datetime.fromtimestamp(created_utc).strftime('%Y-%m-%d %H:%M:%S')

        #print(data)
        #print(f"Utilisateur : {username}")
        #print(f"Créé le : {date_creation}")
        return True
    else:
        #print(f"Erreur : {response.status_code}")
        return False