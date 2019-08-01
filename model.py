from PyQt5.QtCore import QSortFilterProxyModel, pyqtProperty, QAbstractItemModel, QObject, pyqtSignal, QAbstractListModel, Qt, QModelIndex, pyqtSlot, QVariant


class MyItem(QObject):
    nameChanged = pyqtSignal()

    def __init__(self, id, name, lastname, parent=None):
        QObject.__init__(self, parent)
        self._id = id
        self._name = name
        self._lastname = lastname

    @pyqtProperty('QString', notify=nameChanged)
    def id(self):
        return self._id

    @pyqtProperty('QString', notify=nameChanged)
    def name(self):
        return self._name

    @pyqtProperty('QString', notify=nameChanged)
    def lastname(self):
        return self._lastname


class MyModel(QAbstractListModel):
    IdRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2
    LastNameRole = Qt.UserRole + 3
    _roles = {IdRole: b'id', NameRole: b'name', LastNameRole: b'lastname'}

    def __init__(self, parent=None):
        super().__init__(parent)
        self._items = [
            MyItem('1', 'Mitka', 'Braun'),
            MyItem('2', 'Ken', 'Jhon'),
            MyItem('3', 'Bart', 'Simpson'),
            MyItem('4', 'Melany', 'Tramp'),
            MyItem('5', 'Nataly', 'Ivanova'),
            MyItem('6', 'Klaudia', 'Shiffer')
            ]
        self._column_count = 1

    def roleNames(self):
        return self._roles

    def rowCount(self, parent=QModelIndex()):
        return len(self._items)

    def data(self, index, role=Qt.DisplayRole):
        item = self._items[index.row()]
        if role == self.IdRole:
            return item.id
        if role == self.NameRole:
            return item.name
        if role == self.LastNameRole:
            return item.lastname


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
