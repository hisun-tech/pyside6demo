import QtQuick 2.9
        import QtQuick.Controls 2.5
        import QtQuick.Templates 2.12 as T
        import QtQuick.Window 2.2

        Rectangle { // Title Rectangle
        id: titleRect;
        color: "#00A600";
        anchors.top: parent.top;
        anchors.left: parent.left;
        anchors.right: parent.right;
        height: 25;

        TitleButton {   //关闭按钮
            id: closeButtonDialog;
            width: 20;
            height: 18;
            anchors.right: parent.right;
            anchors.verticalCenter: parent.verticalCenter;
            anchors.rightMargin: 2;

        }

        Rectangle {
            id: dragDialog;
            anchors.top: titleRect.top;
            anchors.left: titleRect.left;
            anchors.right: closeButtonDialog.left;
            anchors.bottom: titleRect.bottom;
            color: "darkBlue";

            MouseArea {
                anchors.fill: dragDialog;
                acceptedButtons: Qt.LeftButton;
                property point clickPos: "0,0";
                onPressed: { clickPos = Qt.point(mouse.x,mouse.y);
                }

                onPositionChanged: { //鼠标偏移量 var delta = Qt.point(mouse.x-clickPos.x, mouse.y-clickPos.y);
                    //如果mainwindow继承自QWidget,用setPos
                    self.setX(self.x+delta.x);
                    self.setY(self.y+delta.y);
                }
            }

            Label {
                id: titleWindowLabel;
                anchors.horizontalCenter: parent.horizontalCenter;
                anchors.verticalCenter: parent.verticalCenter;
                color: "#fffffb";
                text: qsTr("用户管理");
                font.bold: true;
            }
        }
    }  // Title Rectangle
