from solid.models.repo import Repo


class RepoParser:

    @classmethod
    def parse(cls, response):
        for index in range(len(response)):
            repo = response[index]
            repo = Repo(repo["id"], repo["name"], repo["stargazers_count"])
            print(repo)
