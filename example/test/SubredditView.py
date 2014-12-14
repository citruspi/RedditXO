__author__ = 'kocsen'

"""
last edited: December 2014
View representation for a subreddit
"""

from PyQt4 import QtGui as QT


class SubredditView(QT.QWidget):
    def __init__(self, subreddit_posts, stack):
        super(SubredditView, self).__init__()

        # set subreddit data here
        self.subreddit_posts = subreddit_posts
        self.uistack = stack

        self.set_layout()
        self.show()

    def clicked(self):
        sender = self.sender()
        text = sender.text()

<<<<<<< HEAD
        if text == 'Back':
            print 'hello'
=======
        if text == 'back':
>>>>>>> b34aa71891dec136cc35f4643bc695b20ec93b69
            # Switch back to group selection
            self.uistack.setCurrentIndex(0)

    def set_layout(self):
        main_grid = QT.QVBoxLayout()
        back_button = QT.QPushButton("Back")
        back_button.clicked.connect(self.clicked)

        main_grid.addWidget(back_button)

<<<<<<< HEAD
        for post in self.subreddit_posts:

            btn = QT.QPushButton(post.title)
            btn.clicked.connect(self.clicked)

            main_grid.addWidget(btn)

=======
>>>>>>> b34aa71891dec136cc35f4643bc695b20ec93b69
        self.setLayout(main_grid)

