from model import TableModel, SortFilterProxyModel
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication
import random


class Main(QQmlApplicationEngine):
    app = QApplication([])

    def __init__(self):
        super().__init__()

        self.tableModel = TableModel('Id', 'Num', 'Str')
        [self.tableModel.addItem(_, random.uniform(-5, 5), f'{_}_str_{_}') for _ in range(10000)]
        self.sortModel = SortFilterProxyModel(self.tableModel)
        self.sortModel.sortend.connect(self.sortEnd)
        self.rootContext().setContextProperty('sortModel', self.sortModel)

        self.tableModel2 = TableModel('Name', 'LastName')
        items = [
            ('Jon', 'Fooo'),
            ('Djorj', 'Cluni'),
            ('Andrey', 'Passar'),
            ('Tilda', 'Svitton'),
            ('Andrea', 'Mutti'),
            ('Ben', 'Stiffler')]
        [self.tableModel2.addItem(item[0], item[1]) for item in items]
        self.sortModel2 = SortFilterProxyModel(self.tableModel2)
        self.sortModel2.sortend.connect(self.sortEnd)
        self.rootContext().setContextProperty('sortModel2', self.sortModel2)

        self.load('main.qml')
        self.footer = self.rootObjects()[0].findChild(QObject, 'footer')
        self.app.exec_()

    def sortEnd(self, items, time):
        self.footer.setProperty('text', f'Sorting {items} items in {time:.2f} sec')


Main()
