from src.module0.TwitterPostDownloader import TwitterPostDownloader
from src.module1.RandomCategorization import RandomCategorization
from src.module2.KeyWordsCategorization import KeyWordsCategorization
from sklearn import metrics
import sys
from sklearn.metrics import accuracy_score
from src.module3.MachineLearningClassifications import MachineLearningCategorizations


def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]


def downloadTestTweets():
    t = TwitterPostDownloader()
    testData = read_words('testTweetIDs')
    category = 'drugs'
    for word in testData:
        if len(word) != 18:
            if (word == 'murders'):
                category = 'murders'
            if (word == 'harassment'):
                category = 'harassment'
            if (word == 'terrorism'):
                category = 'terrorism'
            if (word == 'not_crime'):
                category = 'not_crime'
        else:
            with open(category, 'a') as f:
                f.write(t.getTweetFromTwitter(word).encode("utf-8") + "\n")


def read_sentences(words_file):
    return [word for line in open(words_file, 'r') for word in line.split('\n\'\'')]


def categorizeAndEvaluate():
    trainingSetPathForKW = '../module2/'
    trainingSetPathForML = '../module3/'
    drugs = read_sentences('drugs')
    harassment = read_sentences('harassment')
    murders = read_sentences('murders')
    terrorism = read_sentences('terrorism')
    not_crime = read_sentences('not_crime')
    allCategories = [drugs, harassment, murders, terrorism, not_crime]
    randomCategorization = RandomCategorization()
    keyWordsCategorization = KeyWordsCategorization()
    machineLearningCategorization = MachineLearningCategorizations()
    randomCategorizationResults = []
    keyWordsCategorizationResults = []
    NBCategorizationResults = []
    SGDCategorizationResults = []
    MLPCategorizationResults = []
    NCCategorizationResults = []
    counter = 0
    sys.stdout.write("Processing progress:\n")
    for categories in allCategories:
        for text in categories:
            # randomCategorizationResults.append(randomCategorization.categorize().__getitem__(0))
            # keyWordsCategorizationResults.append(keyWordsCategorization.categorize(text, trainingSetPathForKW))
            # NBCategorizationResults.append(machineLearningCategorization.categorize(text, 'NB', trainingSetPathForML, ))
            # SGDCategorizationResults.append(machineLearningCategorization.categorize(text, 'SGD', trainingSetPathForML))
            MLPCategorizationResults.append(machineLearningCategorization.categorize(text, 'MLP', trainingSetPathForML))
            # NCCategorizationResults.append(machineLearningCategorization.categorize(text, 'NC', trainingSetPathForML))
            sys.stdout.write(" \r%d%%" % counter)
            counter = counter + 1
            sys.stdout.flush()

    listToCompare = createListToCompare()

    # printResultsFor(randomCategorizationResults[0:20], listToCompare[0:20], "drugs", "Random")
    # printResultsFor(keyWordsCategorizationResults[0:20], listToCompare[0:20], "drugs", "Key words ")
    # printResultsFor(NBCategorizationResults[0:20], listToCompare[0:20], "drugs", "Naive bayes")
    # printResultsFor(SGDCategorizationResults[0:20], listToCompare[0:20], "drugs", "SGD")
    # printResultsFor(MLPCategorizationResults[0:20], listToCompare[0:20], "drugs", "Multi layer perception")
    # printResultsFor(NCCategorizationResults[0:20], listToCompare[0:20], "drugs", "Nearest centroid")
    #
    # printResultsFor(randomCategorizationResults[20:40], listToCompare[20:40], "harassment", "Random")
    # printResultsFor(keyWordsCategorizationResults[20:40], listToCompare[20:40], "harassment", "Key words")
    # printResultsFor(NBCategorizationResults[20:40], listToCompare[20:40], "harassment", "Naive bayes")
    # printResultsFor(SGDCategorizationResults[20:40], listToCompare[20:40], "harassment", "SGD")
    # printResultsFor(MLPCategorizationResults[20:40], listToCompare[20:40], "harassment", "Multi layer perception")
    # printResultsFor(NCCategorizationResults[20:40], listToCompare[20:40], "harassment", "Nearest centroid")
    #
    # printResultsFor(randomCategorizationResults[40:60], listToCompare[40:60], "murders", "Random")
    # printResultsFor(keyWordsCategorizationResults[40:60], listToCompare[40:60], "murders", "Key words")
    # printResultsFor(NBCategorizationResults[40:60], listToCompare[40:60], "murders", "Naive bayes")
    # printResultsFor(SGDCategorizationResults[40:60], listToCompare[40:60], "murders", "SGD")
    # printResultsFor(MLPCategorizationResults[40:60], listToCompare[40:60], "murders", "Multi layer perception")
    # printResultsFor(NCCategorizationResults[40:60], listToCompare[40:60], "murders", "Nearest centroid")
    #
    # printResultsFor(randomCategorizationResults[60:80], listToCompare[60:80], "terrorism", "Random")
    # printResultsFor(keyWordsCategorizationResults[60:80], listToCompare[60:80], "terrorism", "Key words")
    # printResultsFor(NBCategorizationResults[60:80], listToCompare[60:80], "terrorism", "Naive bayes")
    # printResultsFor(SGDCategorizationResults[60:80], listToCompare[60:80], "terrorism", "SGD")
    # printResultsFor(MLPCategorizationResults[60:80], listToCompare[60:80], "terrorism", "Multi layer perception")
    # printResultsFor(NCCategorizationResults[60:80], listToCompare[60:80], "terrorism", "Nearest centroid")
    #
    # printResultsFor(randomCategorizationResults[80:100], listToCompare[80:100], "not_crime", "Random")
    # printResultsFor(keyWordsCategorizationResults[80:100], listToCompare[80:100], "not_crime", "Key words")
    # printResultsFor(NBCategorizationResults[80:100], listToCompare[80:100], "not_crime", "Naive bayes")
    # printResultsFor(SGDCategorizationResults[80:100], listToCompare[80:100], "not_crime", "SGD")
    # printResultsFor(MLPCategorizationResults[80:100], listToCompare[80:100], "not_crime", "Multi layer perception")
    # printResultsFor(NCCategorizationResults[80:100], listToCompare[80:100], "not_crime", "Nearest centroid")

    # printResultsFor(randomCategorizationResults, listToCompare, "all", "Random")
    # printResultsFor(keyWordsCategorizationResults, listToCompare, "all", "Key words")
    # printResultsFor(NBCategorizationResults, listToCompare, "all", "Naive bayes")
    # printResultsFor(SGDCategorizationResults, listToCompare, "all", "SGD")
    printResultsFor(MLPCategorizationResults, listToCompare, "all", "Multi layer perception")
    # printResultsFor(NCCategorizationResults, listToCompare, "all", "Nearest centroid")


def createListToCompare():
    listToCompate = []
    categoryToCompare = 'drugs'
    for i in range(0, 100):
        if i == 20:
            categoryToCompare = 'harassment'
        if i == 40:
            categoryToCompare = 'murders'
        if i == 60:
            categoryToCompare = 'terrorism'
        if i == 80:
            categoryToCompare = 'not_crime'
        listToCompate.append(categoryToCompare)
    return listToCompate


def printResultsFor(randomCategorizationResults, listToCompate, categoryName, methodName):
    print "Results for " + categoryName + ":"
    print "==================================================================================================================="
    print  methodName + " categorization:"
    print(metrics.classification_report(formatList(listToCompate), formatList(randomCategorizationResults),
                                        target_names=['drugs', 'harassment', 'murders', 'terrorism', 'not_crime']))
    print "==================================================================================================================="


def formatList(list):
    for n, i in enumerate(list):
        if i == 'drugs':
            list[n] = 0
        if i == 'harassment':
            list[n] = 1
        if i == 'murders':
            list[n] = 2
        if i == 'terrorism':
            list[n] = 3
        if i == 'not_crime':
            list[n] = 4
    return list


if __name__ == '__main__':
    # downloadTestTweets()
    categorizeAndEvaluate()
