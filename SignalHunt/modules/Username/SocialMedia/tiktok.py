import requests

def username(user):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "identity",
        "Accept-Language": "en-US,en;q=0.9",
        "sec-fetch-dest": "document",
        "Connection": "keep-alive",
    }
    url = f"https://www.tiktok.com/@{user}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        if 'statuscode":10221' in response.text.lower():
            print("ok")
