import praw

class Client(object):
    """
    Provides an interface between the GUI and the Reddit API
    """

    connection = None

    def __init__(self):
        """
        Initializes the connection to Reddit with Praw
        """

        useragent = """RedditXO: Empowering XO OLPC users to learn from the
        world."""

        connection = praw.Reddit(useragent)

        self.connection = connection

    def get_group(self, group):
        """
        Returns the top five posts from a predefined group of subreddits
        """

        groups = {
                'science': ['science', 'askscience'],
                'technology': ['technology'],
                'news': ['news', 'worldnews', 'inthenews'],
                'sports': ['sports'],
                'travel': ['travel'],
                'math': ['math', 'learnmath', 'cheatatmathhomework']
        }

        subreddits = '+'.join(groups[group])

        subreddit = self.connection.get_subreddit(subreddits)

        return list(subreddit.get_hot(limit=5))

    def get_subreddit(self, subreddit):
        """
        Returns the top five posts from a single subreddit
        """

        subreddit = self.connection.get_subreddit(subreddit)

        return list(subreddit.get_hot(limit=5))
