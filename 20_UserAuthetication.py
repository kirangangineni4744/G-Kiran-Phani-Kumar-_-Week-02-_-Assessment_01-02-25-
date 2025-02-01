from abc import ABC,abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self):
        print("Logged in using Google")

    def logout(self):
        print("Logged out from Google")

class FacebookAuth(UserAuthentication):
    def login(self):
        print("Logged in using Facebook")

    def logout(self):
        print("Logged out from Facebook")

google_auth=GoogleAuth()
facebook_auth=FacebookAuth()

google_auth.login()
google_auth.logout()

facebook_auth.login()
facebook_auth.logout()
