__author__ = 'kocsen'

"""
last edited: December 2014
View representation for a subreddit
"""


from PyQt4 import QtGui as QT


class SubredditView(QT.QWidget):
    def __init__(self, subreddit_object):
        super(SubredditView, self).__init__()

        # set subreddit data here
        self.subreddit_obj = subreddit_object

        self.set_layout()

    def set_layout(self):
        main_grid = QT.QVBoxLayout()
        back_button = QT.QPushButton("Back")
        main_grid.addWidget(back_button)


        self.setLayout(main_grid)

