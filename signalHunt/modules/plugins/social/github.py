import requests
import sys
import os

import git

from modules.template import BaseSocialMedia
from utils.header import headerHTTP

class Github(BaseSocialMedia):
    pluginWebsite = "github"
    pluginName = "github"
    pluginTags = ["social media", "scraping", "dev"]

    def __init__(self, username: str) -> None:
        super().__init__(username)

        self.username = username
        self.url = f"https://api.github.com/users/{username}"
        
        self.exist = False
        self.requestsSuccessful = False
        self.requestsData = None
        self.elapsed = 0.0

        try: 
            response = requests.get(self.url, headers=headerHTTP(), timeout=5)
            self.elapsed = response.elapsed.total_seconds()

            if response.status_code == 200:
                self.requestsSuccessful = True
                self.exist = True
                self.requestsData = response.json()
            elif response.status_code == 404:
                self.requestsSuccessful = True
                self.exist = False

        except requests.RequestException:
            self.requestsSuccessful = False

    def getAvatar(self) -> str | None:
        if self.exist and self.requestsData:
            return self.requestsData.get("avatar_url")
        return None

    def getHtmlUrl(self) -> str | None:
        if self.exist and self.requestsData:
            return self.requestsData.get("html_url")
        return None

    def getRepos(self)->list |None:
        users = {}
        if self.exist and self.requestsData:
            r  = requests.get(self.requestsData["repos_url"])
            r = r.json()
            for i in r : 
                clone = f"git clone -q {i["ssh_url"]} ./tmp/{i["name"]}" 
                os.system(clone)
                repo = git.Repo(f"./tmp/{i["name"]}")
                for commit in repo.iter_commits(max_count=5):
                    # print(f"Auteur : {commit.author.name} <{commit.author.email}>")

                    if (commit.author.name not in users): #! Mauvaise implementation
                        users[commit.author.name] = [commit.author.email]
                    elif commit.author.email not in users[commit.author.name]:
                        users[commit.author.name].append(commit.author.email)
                        
                os.system(f"rm -rf ./tmp/{i["name"]}")
            return users

        
    def GetEmail(self) -> str:
        return self.getRepos()[self.username]

    def UsernameSearch(self) -> dict:
        if not self.requestsSuccessful:
            return {
                "success": False,
                "message": "Error: bad request"
            }
        return {
            "success": True,
            "message": f"request to {self.pluginName} took {self.elapsed}s",
            "data": {
                "exist": self.exist,
                "website": self.pluginName,
                "tag": self.pluginTags,
                "username": self.username,
                "avatar": self.getAvatar(),
                "htmlUrl": self.getHtmlUrl()
            }
        }

