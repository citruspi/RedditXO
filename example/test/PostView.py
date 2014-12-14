from PyQt4 import QtGui as QT
from PyQt4 import QtCore as core
from PyQt4.QtWebKit import QWebView


class PostView(QT.QWidget):
    def __init__(self, url, stack):
        super(PostView, self).__init__()

        self.url = url
        self.uistack = stack

        self.set_layout()
        # self.show()

    def clicked(self):
        self.uistack.setCurrentIndex(1)
        self.uistack.takeAt(2)

    def set_layout(self):
        main_grid = QT.QVBoxLayout()

        back_button = QT.QPushButton("Back")
        back_button.clicked.connect(self.clicked)
        main_grid.addWidget(back_button)

        webview = QWebView()

        webview.load(core.QUrl(self.url))

        main_grid.addWidget(webview)

        self.setLayout(main_grid)
