from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import load_files
from sklearn.neighbors import NearestCentroid
from sklearn.neural_network import MLPClassifier


class MachineLearningCategorizations:
    def __init__(self):
        self.clfMLP = MLPClassifier(solver='lbfgs', alpha=1e-5,
                                    hidden_layer_sizes=(15,), random_state=1)
        self.clfNB = MultinomialNB()
        self.clfSGD = SGDClassifier()
        self.clfNC = NearestCentroid()


    def categorize(self, tweet, method, trainingSetDataPath):
        trainData = load_files(trainingSetDataPath + 'crime_data')
        # Tokenizing
        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(trainData.data)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

        # Training a classifiers
        self.clfMLP.fit(X_train_tfidf, trainData.target)
        self.clfNB.fit(X_train_tfidf, trainData.target)
        self.clfSGD.fit(X_train_tfidf, trainData.target)
        self.clfNC.fit(X_train_tfidf, trainData.target)

        formattedTweet = [tweet]
        X_new_counts = count_vect.transform(formattedTweet)
        X_new_tfidf = tfidf_transformer.transform(X_new_counts)
        result=-1
        if method == "MLP":
            result = self.categorizeByMLP(X_new_tfidf)
        if method == "NB":
            result = self.categorizeByNB(X_new_tfidf)
        if method == "SGD":
            result = self.categorizeBySGD(X_new_tfidf)
        if method == "NC":
            result = self.categorizeByNC(X_new_tfidf)
        return trainData.target_names[result]


    def categorizeByMLP(self, X_new_tfidf):
        return self.clfMLP.predict(X_new_tfidf)

    def categorizeByNB(self, X_new_tfidf):
        return self.clfNB.predict(X_new_tfidf)

    def categorizeBySGD(self, X_new_tfidf):
        return self.clfSGD.predict(X_new_tfidf)

    def categorizeByNC(self, X_new_tfidf):
        return self.clfNC.predict(X_new_tfidf)
#
# if __name__ == '__main__':
#     MLC = MachineLearningCategorizations()
#     MLC.lowerData()
    # print  MLC.categorize("I will kill church", "MLP","")
