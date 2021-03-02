from solid.repo.reports.html_generator import HTMLGenerator
from solid.repo.reports.markdown_generator import MarkdownGenerator
# from solid.repo.reports_generator_ocp import ReportGenerator
from solid.repo.reports_generator import ReportGenerator
from solid.services.client import GithubClient
from solid.repo.parser import RepoParser

if __name__ == '__main__':
    username = 'HenzoVz'
    response = GithubClient.get_repositorires_by_user(username)

    if response['status'] == 200:
        repos = RepoParser.parse(response['body'])
        markdown_report = ReportGenerator.build(MarkdownGenerator, repos)
        html_report = ReportGenerator.build(HTMLGenerator, repos)
        # markdown_report = ReportGenerator.build("MARKDOWN", repos)
        # html_report = ReportGenerator.build("HTML", repos)

        print(markdown_report)
        print(html_report)
    else:
        print(response['body'])
