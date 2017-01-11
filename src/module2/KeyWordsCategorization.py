import nltk
from nltk.corpus import wordnet as wn


class KeyWordsCategorization:
    def __init__(self):
        self.categories = ['drugs', 'harassment', 'murders', 'terrorism']

    def addMoreWords(self, words_file):
        list = [word for line in open(words_file, 'r') for word in line.split()]
        with open(words_file, "w"):
            pass
        for word in list:
            list = list + self.morphify(word, 'n', 'v')
        list=set(list)
        for word in list:
            with open(words_file, 'a+') as f:
                f.write(word + "\n")

    def read_words(self, words_file):
        return [word for line in open(words_file, 'r') for word in line.split()]

    def categorize(self, tweet, trainingSetPath):
        tknzr = nltk.TweetTokenizer()
        tokens = tknzr.tokenize(tweet)
        # tokens = tknzr.tokenize(tweet.__getitem__(0))

        drugs = self.read_words(trainingSetPath + 'drugs')
        harassment = self.read_words(trainingSetPath + 'harassment')
        murders = self.read_words(trainingSetPath + 'murders')
        terrorism = self.read_words(trainingSetPath + 'terrorism')
        categories_counter_list = [0, 0, 0, 0]

        # Scorer
        for token in tokens:
            if (token in drugs):
                categories_counter_list[0] += 1
            if (token in harassment):
                categories_counter_list[1] += 1
            if (token in murders):
                categories_counter_list[2] += 1
            if (token in terrorism):
                categories_counter_list[3] += 1
        result = categories_counter_list.index(max(categories_counter_list))

        # Results

        # print "Result:"
        if sum(categories_counter_list) == 0:
            # print "Tweet: " + tweet.__getitem__(0) + "=>  " + "No crime detected"
            # print "Text: " + tweet + " => " + "No crime detected"
            return "not_crime"
        else:
            # print "Tweet: " + tweet.__getitem__(0) + "Category: " + categories_list.__getitem__(result)
            # print "Text: " + tweet + " => " + self.categories.__getitem__(result)
            return self.categories.__getitem__(result)

    def morphify(self, word, org_pos, target_pos):
        """ morph a word """
        synsets = wn.synsets(word, pos=org_pos)  # Word not found
        if not synsets:
            return []
        # Get all  lemmas of the word
        lemmas = [l for s in synsets \
                  for l in s.lemmas() if s.name().split('.')[1] == org_pos]
        # Get related forms
        derivationally_related_forms = [(l, l.derivationally_related_forms()) \
                                        for l in lemmas]
        # filter only the targeted pos
        related_lemmas = [l for drf in derivationally_related_forms \
                          for l in drf[1] if l.synset().name().split('.')[1] == target_pos]
        # Extract the words from the lemmas
        words = [l.name() for l in related_lemmas]
        len_words = len(words)
        # Build the result in the form of a list containing tuples (word, probability)
        result = [str(w) for w in set(words)]
        return result


# if __name__ == '__main__':
#     categorization = KeyWordsCategorization()
    # categorization.addMoreWords('drugs')
    # categorization.addMoreWords('harassment')
    # categorization.addMoreWords('murders')
    # categorization.addMoreWords('terrorism')

