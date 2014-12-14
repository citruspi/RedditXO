__author__ = 'kocsen'

"""
last edited: December 2014
View representation for a subreddit
"""

from PyQt4 import QtGui as QT

from PostView import PostView


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
            self.uistack.takeAt(1)
            self.parent().setWindowTitle("RedditXO")

    def set_layout(self):
        main_grid = QT.QVBoxLayout()
        back_button = QT.QPushButton("Back")
        back_button.clicked.connect(self.clicked)

        main_grid.addWidget(back_button)

        for post in self.subreddit_posts:
            post_wid = PostWidget(post, self.uistack)
            # post_wid.clicked.connect(self.clicked)
            main_grid.addWidget(post_wid)

            line = QT.QFrame()
            line.setFrameShape(QT.QFrame.HLine)
            line.setFrameShadow(QT.QFrame.Sunken)
            main_grid.addWidget(line)

        self.setLayout(main_grid)


class PostWidget(QT.QWidget):
    def __init__(self, post_object, stack):
        super(PostWidget, self).__init__()

        self.stack = stack
        self.post = post_object
        self.title = post_object.title
        self.author = str(post_object.author)

        self.set_layout()

    def set_layout(self):
        left_side = QT.QVBoxLayout()
        title_label = QT.QLabel(self.title)
        title_label.setWordWrap(True)
        title_font = QT.QFont("Comic Sans", 10, QT.QFont.Bold)
        title_label.setFont(title_font)

        author_label = QT.QLabel(self.author)
        author_label.setWordWrap(True)
        author_font = QT.QFont("Comic Sans", 8, italic=True)
        author_label.setFont(author_font)
        left_side.addWidget(title_label)
        left_side.addWidget(author_label)

        right_side = QT.QVBoxLayout()
        go_button = QT.QPushButton("View Link")
        go_button.setMaximumWidth(160)
        go_button.clicked.connect(self.go_to_link_action)
        comments_button = QT.QPushButton("Comment")
        comments_button.setMaximumWidth(160)
        comments_button.clicked.connect(self.go_to_comments_action)
        right_side.addWidget(go_button)
        right_side.addWidget(comments_button)

        a_level_layout = QT.QHBoxLayout()
        a_level_layout.addLayout(left_side)
        a_level_layout.addLayout(right_side)

        self.setLayout(a_level_layout)

    def go_to_link_action(self):
        post_view_widget = PostView(self.post.url, self.stack)
        self.change_view_to(post_view_widget)

    def go_to_comments_action(self):
        post_view_widget = PostView(self.post.permalink, self.stack)
        self.change_view_to(post_view_widget)


    def change_view_to(self, widget):
        self.stack.addWidget(widget)
        self.stack.setCurrentIndex(2)