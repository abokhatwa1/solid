from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class MultiFunctionDevice(Printer, Scanner):
    def print(self):
        return "Printing document"

    def scan(self):
        return "Scanning document"

class SimplePrinter(Printer):
    def print(self):
        return "Printing only"

printer = SimplePrinter()
print(printer.print()) 