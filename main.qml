import QtQuick 2.1
import QtQuick.Controls 1.1
import MyModel 1.0
import SortFilterProxyModel 1.0

ApplicationWindow {
    width: 400
    height: 200
    visible: true
    title: "qml-tableview-sort"

    Rectangle {
        anchors.fill: parent

        MyModel {
            id: mymodel
        }

        SortFilterProxyModel {
            id: proxyModel
            source: mymodel
        }

        TableView {
            id: tableView
            anchors.fill: parent
            model: proxyModel
            sortIndicatorVisible: true
            onSortIndicatorOrderChanged: model.sort(getColumn(sortIndicatorColumn).role, sortIndicatorOrder)
            onSortIndicatorColumnChanged: model.sort(getColumn(sortIndicatorColumn).role, sortIndicatorOrder)
            TableViewColumn {
                title: "#"
                role: "id"
                width: 50
            }
            TableViewColumn {
                title: "Name"
                role: "name"
            }
            TableViewColumn {
                title: "Last Name"
                role: "lastname"
            }
        }

    }
}
