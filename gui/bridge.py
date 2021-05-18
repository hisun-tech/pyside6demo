# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: bridge.py
  @time: 2021/5/18 10:29
  @desc:
"""

import sys
import os
from pathlib import Path

from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from style_rc import *


class Bridge(QObject):

    @Slot(str, result=str)
    def getColor(self, color_name):
        if color_name.lower() == "red":
            return "#ef9a9a"
        elif color_name.lower() == "green":
            return "#a5d6a7"
        elif color_name.lower() == "blue":
            return "#90caf9"
        else:
            return "white"

    @Slot(float, result=int)
    def getSize(self, s):
        size = int(s * 42)
        if size <= 0:
            return 1
        else:
            return size

    @Slot(str, result=bool)
    def getItalic(self, s):
        if s.lower() == "italic":
            return True
        else:
            return False

    @Slot(str, result=bool)
    def getBold(self, s):
        if s.lower() == "bold":
            return True
        else:
            return False

    @Slot(str, result=bool)
    def getUnderline(self, s):
        if s.lower() == "underline":
            return True
        else:
            return False


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Instance of the Python object
    bridge = Bridge()

    # Expose the Python object to QML
    context = engine.rootContext()
    context.setContextProperty("con", bridge)

    # Get the path of the current directory, and then add the name
    # of the QML file, to load it.
    qmlFile = Path(__file__).parent / 'view.qml'
    engine.load(os.fspath(qmlFile.resolve()))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
