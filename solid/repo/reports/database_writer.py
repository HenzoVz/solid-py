from solid.repo.reports.interface_write import InterfaceWrite


class ReportDatabaseWriter(InterfaceWrite):

    @staticmethod
    def write(report):
        print("salvando report no banco")
