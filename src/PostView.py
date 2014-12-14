from PyQt4 import QtGui as QT
from PyQt4 import QtCore as core
from PyQt4.QtWebKit import QWebView


class PostView(QT.QWidget):
    """
    Represents the post view and renders a web view with the post or comments
    responding to the post
    """

    def __init__(self, url, stack):
        """
        Initializes a widget with a back button and a web view
        
        :return:
        """

        super(PostView, self).__init__()

        self.url = url
        self.uistack = stack

        self.set_layout()

    def clicked(self):
        """
        Handles the back button being clicked

        :return:
        """

        self.uistack.setCurrentIndex(1)
        self.uistack.takeAt(2)

    def set_layout(self):
        """
        Lays out the post view with a back button and a webview under it

        :return:
        """

        main_grid = QT.QVBoxLayout()

        # Creates a back button for returning to the previous view
        back_button = QT.QPushButton("Back")
        back_button.clicked.connect(self.clicked)
        main_grid.addWidget(back_button)

        # Creates a web view and loads the URL passed to the post view
        webview = QWebView()

        webview.load(core.QUrl(self.url))

        main_grid.addWidget(webview)

        self.setLayout(main_grid)
