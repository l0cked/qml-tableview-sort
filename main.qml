import QtQuick 2.1
import QtQuick.Controls 1.6
import QtQuick.Layouts 1.3


ApplicationWindow {
    width: 1000
    height: 400
    visible: true
    title: "qml-tableview-sort"
    ColumnLayout {
        anchors.fill: parent
        spacing: 0
        RowLayout {
            Layout.fillWidth: true
            Layout.fillHeight: true
            spacing: 0
            TableView {
                model: sortModel
                Layout.fillWidth: true
                Layout.fillHeight: true
                alternatingRowColors: false
                sortIndicatorVisible: true
                onSortIndicatorOrderChanged: model.sort(sortIndicatorColumn, sortIndicatorOrder)
                onSortIndicatorColumnChanged: model.sort(sortIndicatorColumn, sortIndicatorOrder)
                TableViewColumn {
                    title: "#"
                    role: "id"
                }
                TableViewColumn {
                    title: "Number"
                    role: "num"
                }
                TableViewColumn {
                    title: "String"
                    role: "str"
                }
            }
            TableView {
                model: sortModel2
                Layout.fillWidth: true
                Layout.fillHeight: true
                alternatingRowColors: false
                sortIndicatorVisible: true
                onSortIndicatorOrderChanged: model.sort(sortIndicatorColumn, sortIndicatorOrder)
                onSortIndicatorColumnChanged: model.sort(sortIndicatorColumn, sortIndicatorOrder)
                TableViewColumn {
                    title: "Datetime"
                    role: "dt"
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
        Rectangle {
            Layout.fillWidth: true
            height: 18
            color: "transparent"
            Text {
                objectName: "footer"
                anchors.fill: parent
                anchors.leftMargin: 10
                verticalAlignment: Text.AlignVCenter
                text: "Ready"
                renderType: Text.NativeRendering
            }
        }
    }
}
