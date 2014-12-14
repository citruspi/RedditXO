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

        if text == 'Back':
            # Switch back to group selection
            self.uistack.setCurrentIndex(0)

    def set_layout(self):
        main_grid = QT.QVBoxLayout()
        back_button = QT.QPushButton("Back")
        back_button.clicked.connect(self.clicked)

        main_grid.addWidget(back_button)

        for post in self.subreddit_posts:
            btn = QT.QPushButton(post.title)
            btn.clicked.connect(self.clicked)

            main_grid.addWidget(btn)

        self.setLayout(main_grid)


class PostWidget(QT.QWidget):
    def __init__(self, post_object):
        super(PostWidget, self).__init__()

        self.title = post_object.title
        self.author = post_object.author.user_name

        self.set_layout()
        self.show()

    def set_layout(self):
        left_side = QT.QVBoxLayout()
        title_label = QT.QLabel(self.title)
        author_label = QT.QLabel(self.author)
        left_side.addWidget(title_label)
        left_side.addWidget(author_label)

        right_side = QT.QHBoxLayout()
        go_button = QT.QPushButton("View Link")
        comments_button = QT.QPushButton("View Comments")
        right_side.addWidget(go_button)
        right_side.addWidget(comments_button)

        a_level_layout = QT.QHBoxLayout()
        a_level_layout.addLayout(left_side)
        a_level_layout.addLayout(right_side)

