import requests
import json


class ListRepositories():
    API_BASE_URL = 'http://api.github.com'

    def __init__(self, user):
        self._user = user

    def get_repositorires_by_user(self):
        response = requests.get(f'{self.API_BASE_URL}/users/{self._user}/repos')

        if response.status_code == 200:
            return {"status": 200, "body": response.json()}
        else:
            return {"status": response.status_code, "body": 'Error while getting repos'}

    def parse_response(self):
        response = self.get_repositorires_by_user()
        body = response['body']
        if response['status'] == 200:
            for index in range(len(body)):
                print(f'{body[index]["id"]} - {body[index]["name"]} - {body[index]["stargazers_count"]}')


repos = ListRepositories('HenzoVz')
repos.parse_response()
