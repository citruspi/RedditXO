import praw

class Client(object):

    connection = None

    def __init__(self):

        useragent = """RedditXO: Empowering the poor bastards with XO OLPC's to
        read Reddit."""

        connection = praw.Reddit(useragent)

        self.connection = connection
