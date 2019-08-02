from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QAbstractListModel, QSortFilterProxyModel, QModelIndex
import time


class TableModel(QAbstractListModel):
    def __init__(self, *roles):
        super().__init__()
        self.roles = {}
        self.items = []
        n = 0
        for role in roles:
            n += 1
            value = Qt.UserRole + n
            setattr(self, role+'Role', value)
            self.roles[value] = bytes(role.lower(), encoding='utf8')

    def roleNames(self):
        return self.roles

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def data(self, index, role=Qt.DisplayRole):
        if role in self.roles:
            return self.items[index.row()][self.roles[role].decode()]

    @pyqtSlot(tuple)
    def addItem(self, item):
        self.addItems([item])

    @pyqtSlot(list)
    def addItems(self, items):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        for item in items:
            newitem = {}
            n = 0
            for key, role in self.roles.items():
                try:
                    value = float(item[n])
                except:
                    value = str(item[n])
                newitem[role.decode()] = value
                n += 1
            self.items.append(newitem)
        self.endInsertRows()


class SortFilterProxyModel(QSortFilterProxyModel):
    sortend = pyqtSignal(int, float)

    def __init__(self, source):
        super().__init__()
        self.setSourceModel(source)
        self.source = source

    @pyqtSlot(int, int)
    def sort(self, column, order):
        start = time.time()
        key = list(self.source.roles)[column]

        self.currentSortRole = self.source.roles[key].decode()

        self.setSortRole(key)
        super().sort(0, order)
        self.sortend.emit(len(self.source.items), time.time()-start)

    def lessThan(self, left, right):
        if self.source.items[left.row()][self.currentSortRole] < self.source.items[right.row()][self.currentSortRole]:
            return True
        return False
