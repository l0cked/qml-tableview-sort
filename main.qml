import QtQuick 2.1
import QtQuick.Controls 1.1


ApplicationWindow {
    width: 450
    height: 200
    visible: true
    title: "qml-tableview-sort"

    Rectangle {
        anchors.fill: parent

        TableView {
            id: tableView
            anchors.fill: parent
            model: tableModel
            sortIndicatorVisible: true
            onSortIndicatorOrderChanged: model.sort(sortIndicatorColumn, sortIndicatorOrder)
            onSortIndicatorColumnChanged: model.sort(sortIndicatorColumn, sortIndicatorOrder)
            TableViewColumn {
                title: "#"
                role: "id"
                width: 50
            }
            TableViewColumn {
                title: "Number"
                role: "num"
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
