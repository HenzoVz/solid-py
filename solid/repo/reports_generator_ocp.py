from .reports.html_generator import HTMLGenerator
from .reports.markdown_generator import MarkdownGenerator

# metodo da classe não respeita o principio do aberto fechado, pois esta aberto para modificações
class ReportGenerator:

    @classmethod
    def build(cls, type, repos):
        if type == 'HTML':
            return HTMLGenerator.build(repos)
        elif type == 'MARKDOWN':
            return MarkdownGenerator.build(repos)
        else:
            return "Invalid report type"
