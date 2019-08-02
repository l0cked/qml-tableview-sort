from datetime import datetime
from model import TableModel, SortFilterProxyModel
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication
import random
import time


class Main(QQmlApplicationEngine):
    def __init__(self):
        start = time.time()
        self.app = QApplication([])
        super().__init__()

        self.tableModel = TableModel('Id', 'Num', 'Str')
        self.tableModel.addItem((-1, 0, 'Test .addItem()'))
        self.tableModel.addItems([(_, random.uniform(-5, 5), f'{_}_str_{_}') for _ in range(10000)])
        self.sortModel = SortFilterProxyModel(self.tableModel)
        self.sortModel.sortend.connect(self.sortEnd)
        self.rootContext().setContextProperty('sortModel', self.sortModel)

        self.tableModel2 = TableModel('Dt', 'Name', 'LastName')
        self.tableModel2.addItems([(self.rndDt(), self.rndWorld(), self.rndWorld()) for _ in range(10000)])
        self.sortModel2 = SortFilterProxyModel(self.tableModel2)
        self.sortModel2.sortend.connect(self.sortEnd)
        self.rootContext().setContextProperty('sortModel2', self.sortModel2)

        self.load('main.qml')
        self.footer = self.rootObjects()[0].findChild(QObject, 'footer')
        self.footer.setProperty('text', f'Initialization in {time.time()-start:.2f} sec')
        self.app.exec_()

    def rndDt(self):
        return datetime.fromtimestamp(random.randint(1, int(time.time())))

    def rndWorld(self):
        big = 'ABCDEFGHIKLMNOPQRSTVXYZ'
        chrs = 'abcdefghiklmnopqrstvxyz'
        return big[random.randint(0, len(big)-1)] + ''.join(random.choice(chrs) for _ in range(random.randint(4, 10)))

    def sortEnd(self, items, time):
        self.footer.setProperty('text', f'Sorting {items} items in {time:.2f} sec')


Main()
