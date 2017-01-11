import random


class RandomCategorization:
    def __init__(self):
        self.categories = ["drugs", "murders", "terrorism", "harassment", "not_crime"]

    def categorize(self):
        # with open('../module0/downloaded_post.tsv', 'r') as f:
        #     tweet = [f.read()]
        return random.sample(self.categories, 1)

