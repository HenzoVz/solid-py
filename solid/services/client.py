import requests


class GithubClient:
    API_BASE_URL = 'http://api.github.com'

    def __init__(self, user):
        self._user = user

    @classmethod
    def get_repositorires_by_user(self, user):
        response = requests.get(f'{self.API_BASE_URL}/users/{user}/repos')

        if response.status_code == 200:
            return {"status": 200, "body": response.json()}
        else:
            return {"status": response.status_code, "body": 'Error while getting repos'}