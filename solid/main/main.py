from solid.services.client import GithubClient
from solid.repo.parser import RepoParser

if __name__ == '__main__':
    username = 'HenzoVz'
    response = GithubClient.get_repositorires_by_user(username)

    if response['status'] == 200:
        RepoParser.parse(response['body'])
    else:
        print(response['body'])
