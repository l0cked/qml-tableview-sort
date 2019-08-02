from PyQt5.QtCore import pyqtProperty, pyqtSlot, QSortFilterProxyModel, QAbstractItemModel, QAbstractListModel, Qt, QModelIndex


class TableModel(QAbstractListModel):
    IdRole = Qt.UserRole + 1
    NumRole = Qt.UserRole + 2
    NameRole = Qt.UserRole + 3
    LastNameRole = Qt.UserRole + 4
    _roles = {
        IdRole: b'id',
        NumRole: b'num',
        NameRole: b'name',
        LastNameRole: b'lastname'}

    def __init__(self):
        super().__init__()
        self.items = [
            {'id': '1', 'num': '17', 'name': 'Angel', 'lastname': 'Braun'},
            {'id': '2', 'num': '18', 'name': 'Bart', 'lastname': 'Jhon'},
            {'id': '3', 'num': '19', 'name': 'Cecil', 'lastname': 'Simpson'},
            {'id': '4', 'num': '20', 'name': 'Dart', 'lastname': 'Tramp'},
            {'id': '5', 'num': '121', 'name': 'Evgen', 'lastname': 'Ivanova'},
            {'id': '6', 'num': '22', 'name': 'Klaudia', 'lastname': 'Shiffer'},
            {'id': '23', 'num': '23', 'name': 'Test', 'lastname': 'Fail'},
            {'id': '1123', 'num': '.01', 'name': 'Olya', 'lastname': 'BigTits'},
            ]

    def roleNames(self):
        return self._roles

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == self.IdRole:
            return self.items[row]['id']
        if role == self.NumRole:
            return self.items[row]['num']
        if role == self.NameRole:
            return self.items[row]['name']
        if role == self.LastNameRole:
            return self.items[row]['lastname']


class SortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super().__init__()

    @pyqtProperty(QAbstractItemModel)
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        self.setSourceModel(source)
        self._source = source

    @pyqtSlot(int, int)
    def sort(self, column, order):
        self._column = column
        key = list(self._source._roles)[column]
        self._role = self._source._roles[key].decode("utf-8")
        self.setSortRole(key)
        super().sort(0, order)

    def lessThan(self, left, right):
        l = left.row()
        r = right.row()
        i = self._source.items
        try:
            if int(i[l][self._role]) < int(i[r][self._role]):
                return True
            return False
        except:
            pass
        if i[l][self._role] < i[r][self._role]:
            return True
        return False
