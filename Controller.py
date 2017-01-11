import os
from flask import Flask, render_template, request, redirect
from react.render import render_component
from src.module1.RandomCategorization import RandomCategorization
from src.module2.KeyWordsCategorization import KeyWordsCategorization
from src.module0.TwitterPostDownloader import TwitterPostDownloader
from src.module3.MachineLearningClassifications import MachineLearningCategorizations

DEBUG = True

app = Flask(__name__)
app.debug = DEBUG

results = []


@app.route('/')
def index():
    rendered = render_component(
        os.path.join(os.getcwd(), 'static', 'js', 'CategorizationBox.jsx'),
        {
            'results': results,
            'url': '/categorize/',
        },
        to_static_markup=True,
    )

    return render_template('index.html', rendered=rendered)


@app.route('/categorize/', methods=('POST',))
def categorize():
    t = TwitterPostDownloader()
    tweet = t.getTweetFromTwitter(request.form['tweetID'])

    categorizationResult = chooseMethodAndCategorize(str(request.form["categorizationMethod"]), tweet)
    if  isinstance(categorizationResult[0],list):
        categorizationResult[0]=categorizationResult[0].__getitem__(0)
    results.insert(0,{
        'tweetID': tweet,
        'text': "Result: " + categorizationResult[0] + " detected by " + categorizationResult[1],
    })

    return redirect('/')


def chooseMethodAndCategorize(method, tweet):
    trainingSetDataPathForKW='src/module2/'
    trainingSetDataPathForML='src/module3/'

    if (method == "R"):
        result = RandomCategorization().categorize(tweet)
        message = "Random method"
    elif (method == "KW"):
        result = KeyWordsCategorization().categorize(tweet,trainingSetDataPathForKW)
        message = "Key words method"
    elif (method == "NB"):
        result = MachineLearningCategorizations().categorize(tweet, method,trainingSetDataPathForML)
        message = "Naive bayes classifier method"
    elif (method == "SGD"):
        result = MachineLearningCategorizations().categorize(tweet, method,trainingSetDataPathForML)
        message = "Stochastic gradient descent classifier method"
    elif (method == "NC"):
        result = MachineLearningCategorizations().categorize(tweet, method,trainingSetDataPathForML)
        message = "Nearest Centroid classifier method"
    elif (method == "MLP"):
        result = MachineLearningCategorizations().categorize(tweet, method,trainingSetDataPathForML)
        message = "Multilayer perception classifier method"
    else:
        return ""
    return [result,message]


if __name__ == '__main__':
    app.run()
