from abc import ABC, abstractmethod

class BaseSocialMedia(ABC):
    name: str ="username" # nom du plugin

    def __init__(self, username: str):
        self.username = username

    @abstractmethod
    def API(self):
        pass