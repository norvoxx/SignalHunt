from abc import ABC, abstractmethod

class BaseSocialMedia(ABC):
    pluginName: str = "username" 
    def __init__(self, username: str):
        self.username = username

    @abstractmethod
    def UsernameSearch(self):
        pass