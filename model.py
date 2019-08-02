from PyQt5.QtCore import Qt, pyqtSlot, QAbstractListModel, QSortFilterProxyModel


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
    _items = [
        {'id': '1', 'num': '17', 'name': 'Angel', 'lastname': 'Braun'},
        {'id': '2', 'num': '18', 'name': 'Bart', 'lastname': 'Jhon'},
        {'id': '3', 'num': '1', 'name': 'Cecil', 'lastname': 'Simpson'},
        {'id': '4', 'num': '20', 'name': 'Dart', 'lastname': 'Tramp'},
        {'id': '5', 'num': '121', 'name': 'Evgen', 'lastname': 'Ivanova'},
        {'id': '6', 'num': '1.22', 'name': 'Klaudia', 'lastname': 'Shiffer'},
        {'id': '23', 'num': '.02', 'name': 'Test', 'lastname': 'Fail'},
        {'id': '1123', 'num': '.01', 'name': 'Olya', 'lastname': 'BigTits'}]

    def __init__(self):
        super().__init__()

    def roleNames(self):
        return self._roles

    def rowCount(self, parent):
        return len(self._items)

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == self.IdRole:
            return self._items[row]['id']
        if role == self.NumRole:
            return self._items[row]['num']
        if role == self.NameRole:
            return self._items[row]['name']
        if role == self.LastNameRole:
            return self._items[row]['lastname']


class SortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, source):
        super().__init__()
        self.setSourceModel(source)
        self._source = source

    @pyqtSlot(int, int)
    def sort(self, column, order):
        roles = self._source._roles
        key = list(roles)[column]

        self._column = column
        self._role = roles[key].decode()

        self.setSortRole(key)
        super().sort(0, order)

    def lessThan(self, left, right):
        l = left.row()
        r = right.row()
        i = self._source._items
        try:
            if int(i[l][self._role]) < int(i[r][self._role]):
                return True
            return False
        except:
            pass
        if i[l][self._role] < i[r][self._role]:
            return True
        return False
