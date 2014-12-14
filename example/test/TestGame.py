#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
last edited: December 2014
Reddit XO Main entry point for QT program
"""

import sys

from PyQt4 import QtGui

import reddit
from SubredditView import SubredditView


class Reddit(QtGui.QWidget):
    """
    The main Entry point of the RedditXO Program.
    This is actually the QT Widget that starts up the
    main home page.
    """

    def __init__(self):
        """
        Inits a QWidget. Also instantiates a client
        which is the API that interacts with Reddit.com

        Finally inits the UI with layouts and stuff.
        :return:
        """
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
        """
        Sets up the layout and the general view for the main page.

        It also centers the windows and sets some main properties like the title
        :return:
        """

        self.set_layout()

        self.center()
        self.setWindowTitle('RedditXO')

        # Finally, show it
        self.show()

    def set_layout(self):
        """
        Sets the specific main layouts.
        The layout structure is all parented by a STACKED LAYOUT.
        The Stack layout is to have at most 2 widgets stacked. The first widget (@ index 0) is
        the main page and the second stacked widget is the subreddit page.

        :return:
        """
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
                button.setStyleSheet('font-size: 18pt; font-family: ComicSans;')
                button.clicked.connect(self.group_selected)
                grid.addWidget(button, *position)

        front_page_wid = QtGui.QWidget()
        front_page_wid.setLayout(main_grid)

        main_stack.addWidget(front_page_wid)
        self.main_stack = main_stack

        self.setLayout(main_stack)

    def group_selected(self):
        """
        Button Listener
        Listens to the buttons clicked on the main page.
        Given the button, will ask the client to perform the data fetch.
        With the data, create a subreddit view widget and add it to the stack.

        Then switch the stack back.
        :return:
        """

        sender = self.sender()

        group = str(sender.text())

        posts = self.client.get_group(self.subreddits[group])
        subreddit_widget = SubredditView(posts, self.main_stack)
        self.main_stack.addWidget(subreddit_widget)
        self.main_stack.setCurrentIndex(1)

    def center(self):
        """
        Responsible for the main geometry of the system, and then centering it.
        :return:
        """
        self.resize(100 * 2, 150 * 3)
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    """
    Start the app, set the system close.
    :return:
    """
    app = QtGui.QApplication(sys.argv)
    reddit = Reddit()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()     
