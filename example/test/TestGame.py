#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
last edited: October 2014
Reddit XO Main entry point for QT program
"""

import sys

from PyQt4 import QtGui


class Reddit(QtGui.QWidget):
    def __init__(self):
        super(Reddit, self).__init__()
        self.subreddits = {
            "Science": "science",
            "Technology": "Technology",
            "World News": "Worldnews",
            "Local News": "Loalnews",
            "Sports": "sports",
            "Travel": "travel",
            "Math":"",
            "English":"",
            "Secret":""
        }

        self.initUI()

    def initUI(self):
        self.fetch_data()
        self.set_layout()

        self.center()
        self.setWindowTitle('RedditXO')

        # Finally, show it
        self.show()

    def set_layout(self):
        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        positions = [(i,j) for i in range(5) for j in range(2)]
        for position, name in zip(positions, self.subreddits):

            if name == '':
                continue
            button = QtGui.QPushButton(name)
            grid.addWidget(button, *position)

    def center(self):
        self.resize(250 * 4, 150 * 4)
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def fetch_data(self):
        pass


def main():
    app = QtGui.QApplication(sys.argv)
    reddit = Reddit()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()     