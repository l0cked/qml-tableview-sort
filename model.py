from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QSortFilterProxyModel, QAbstractItemModel, QObject, QAbstractListModel, Qt, QModelIndex, QVariant


class MyModel(QAbstractListModel):
    IdRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2
    LastNameRole = Qt.UserRole + 3
    roles = {
        IdRole: b'id',
        NameRole: b'name',
        LastNameRole: b'lastname'}

    def __init__(self, parent=None):
        super().__init__(parent)
        self.items = [
            {'id': '1', 'name': 'Mitka', 'lastname': 'Braun'},
            {'id': '2', 'name': 'Ken', 'lastname': 'Jhon'},
            {'id': '3', 'name': 'Bart', 'lastname': 'Simpson'},
            {'id': '4', 'name': 'Melany', 'lastname': 'Tramp'},
            {'id': '5', 'name': 'Nataly', 'lastname': 'Ivanova'},
            {'id': '6', 'name': 'Klaudia', 'lastname': 'Shiffer'}]

    def roleNames(self):
        return self.roles

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == self.IdRole:
            return self.items[row]['id']
        if role == self.NameRole:
            return self.items[row]['name']
        if role == self.LastNameRole:
            return self.items[row]['lastname']


class SortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent):
        super().__init__(parent)

    @pyqtProperty(QAbstractItemModel)
    def source (self):
        return self._source

    @source.setter
    def source (self, source):
        self.setSourceModel(source)
        self._source = source

    def roleKey(self, role):
        roles = self.roleNames()
        for key, value in roles.items():
            if value == role:
                return key
        return -1

    @pyqtSlot(str, int)
    def sort(self, role, order):
        self.setSortRole(self.roleKey(role));
        super().sort(0, order);
