class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Report data: {self.data}"

class ReportPrinter:
    def print_report(self, report):
        print(report.generate())

report = Report("Sales Data")
printer = ReportPrinter()
printer.print_report(report)