from PyQt4 import QtGui as QT

class PostView(QT.QWidget):

    def __init__(self, post, stack):

        super(PostView, self).__init__()

        self.post = post
        self.uistack = stack

        self.set_layout()
        self.show()

    def set_layout(self):

        main_grid = QT.QVBoxLayout()

        webview = QT.QWebView()

        webview.load(QT.QUrl(post.url))

        main_grid.addWidget(webview)

        self.setLayout(main_grid)
