import praw

class Client(object):

    connection = None

    def __init__(self):

        useragent = """RedditXO: Empowering the poor bastards with XO OLPC's to
        read Reddit."""

        connection = praw.Reddit(useragent)

        self.connection = connection

    def get_group(self, group):

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

        return subreddit.get_hot(limit=10)


    def get_subreddit(self, subreddit):

        subreddit = self.connection.get_subreddit(subreddit)

        return subreddit.get_hot(limit=10)
