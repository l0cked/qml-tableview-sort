from datetime import datetime
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QAbstractListModel, QSortFilterProxyModel, QModelIndex, QDateTime
import time


class TableModel(QAbstractListModel):
    def __init__(self, *roles):
        super().__init__()
        self.roles = {}
        self.rows = []
        n = 0
        for role in roles:
            n += 1
            value = Qt.UserRole + n
            setattr(self, role+'Role', value)
            self.roles[value] = bytes(role.lower(), encoding='utf8')

    def roleNames(self):
        return self.roles

    def rowCount(self, parent=QModelIndex()):
        return len(self.rows)

    def data(self, index, role=Qt.DisplayRole):
        if role in self.roles:
            ret = self.rows[index.row()][self.roles[role].decode()]
            if type(ret) == QDateTime:
                return ret.toString('dd-MM-yyyy HH:mm:ss')
            return ret

    @pyqtSlot(tuple)
    def addRow(self, row):
        self.addRows([row])

    @pyqtSlot(list)
    def addRows(self, rows):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        for row in rows:
            item = {}
            n = 0
            for key, role in self.roles.items():
                value = None
                data = row[n]
                try:
                    value = float(data)
                except:
                    value = QDateTime.fromString(str(data), 'yyyy-MM-dd HH:mm:ss')
                    if not value:
                        value = str(data)
                item[role.decode()] = value
                n += 1
            self.rows.append(item)
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
        self.sortend.emit(len(self.source.rows), time.time()-start)

    def lessThan(self, left, right):
        if self.source.rows[left.row()][self.currentSortRole] < self.source.rows[right.row()][self.currentSortRole]:
            return True
        return False
