from model import TableModel, SortFilterProxyModel
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication


class Main(QQmlApplicationEngine):
    app = QApplication([])

    def __init__(self):
        super().__init__()
        self.tableModel = SortFilterProxyModel(TableModel())
        self.rootContext().setContextProperty('tableModel', self.tableModel)
        self.load('main.qml')
        self.app.exec_()


Main()
