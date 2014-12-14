#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
last edited: October 2014
Reddit XO Main entry point for QT program
"""

import sys

from PyQt4 import QtGui
import reddit

class Reddit(QtGui.QWidget):
    def __init__(self):
        super(Reddit, self).__init__()

        self.subreddits = {
            "Science": "science",
            "Technology": "technology",
            "News": "news",
            "Sports": "sports",
            "Travel": "travel",
            "Math": "math",
        }

        self.client = reddit.Client()

        self.initUI()

    def initUI(self):

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

        positions = [(i, j) for i in range(4) for j in range(2)]
        for position, name in zip(positions, self.subreddits):

            if name != '':
                button = QtGui.QPushButton(name)
                button.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
                button.setStyleSheet('font-size: 20pt; font-family: ComicSans;')
                button.clicked.connect(self.group_selected)
                grid.addWidget(button, *position)

        front_page_wid = QtGui.QWidget()
        front_page_wid.setLayout(main_grid)

        subreddit_wid = QtGui.QWidget()

        main_stack.addWidget(front_page_wid)
        main_stack.addWidget(subreddit_wid)

        self.setLayout(main_stack)

    def group_selected(self):

        sender = self.sender()

        group = str(sender.text())

        posts = self.client.get_group(self.subreddits[group])


    def center(self):
        self.resize(230 * 2, 150 * 3)
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QtGui.QApplication(sys.argv)
    reddit = Reddit()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()     
