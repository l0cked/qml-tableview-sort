from model import MyModel, SortFilterProxyModel
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtWidgets import QApplication


class Main(QQmlApplicationEngine):
    app = QApplication([])

    def __init__(self):
        super().__init__()
        qmlRegisterType(MyModel, 'MyModel', 1, 0, 'MyModel')
        qmlRegisterType(SortFilterProxyModel, 'SortFilterProxyModel', 1, 0, 'SortFilterProxyModel')
        self.load('main.qml')
        self.app.exec_()


Main()
