from solid.repo.reports.html_generator import HTMLGenerator
from solid.repo.reports.markdown_generator import MarkdownGenerator
# from solid.repo.reports_generator_ocp import ReportGenerator
from solid.repo.reports_generator import ReportGenerator
from solid.services.client import GithubClient
from solid.repo.parser import RepoParser
from solid.repo.reports.file_writer import ReportFileWriter
from solid.repo.reports.database_writer import ReportDatabaseWriter
from solid.repo.reports.writer import ReportWriter

from solid.models.member import Member
from solid.models.manager_lsp import Manager

if __name__ == '__main__':
    username = 'murilohenzo'
    response = GithubClient.get_repositorires_by_user(username)

    if response['status'] == 200:
        repos = RepoParser.parse(response['body'])
        markdown_report = ReportGenerator.build(MarkdownGenerator, repos)
        html_report = ReportGenerator.build(HTMLGenerator, repos)

        print(markdown_report)
        print(html_report)

        # markdown_report = ReportGenerator.build("MARKDOWN", repos)
        # html_report = ReportGenerator.build("HTML", repos)
        ReportWriter.write(markdown_report, ReportFileWriter)
        ReportWriter.write(markdown_report, ReportDatabaseWriter)

    else:
        print(response['body'])

    member = Member("johndoe", "johndoe@example.com")

    print(member.members())
