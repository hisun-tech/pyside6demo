# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: main_window.py
  @time: 2021/5/18 10:20
  @desc:
"""
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl

app = QApplication([])
view = QQuickView()
url = QUrl("view.qml")

view.setSource(url)
view.showMaximized()
app.exec()
