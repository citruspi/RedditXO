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
            "Sports": "sports",
            "Travel": "travel",
            "Math": "",
            "English": "",
            "Funny": ""
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
        main_stack = QtGui.QStackedLayout()

        main_grid = QtGui.QVBoxLayout()
        welcome_wid = QtGui.QLabel(
            "Hello! Welcome to RedditXO, a great way to browse recent news and updates on the world. From the people to the people")
        main_grid.addWidget(welcome_wid)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        main_grid.addLayout(grid)
        # stack.addChildLayout(grid)
        # self.setLayout(grid)


        positions = [(i, j) for i in range(4) for j in range(2)]
        for position, name in zip(positions, self.subreddits):

            if name != '':
                button = QtGui.QPushButton(name)
                button.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
                button.setStyleSheet('font-size: 20pt; font-family: ComicSans;')
                grid.addWidget(button, *position)

        self.setLayout(main_grid)

    def center(self):
        self.resize(230 * 2, 150 * 3)
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