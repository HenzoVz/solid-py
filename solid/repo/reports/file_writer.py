from solid.repo.reports.interface_write import InterfaceWrite


class ReportFileWriter(InterfaceWrite):

    @staticmethod
    def write(report):
        file = open('report.txt', 'w')
        file.write(report)
        file.close()
