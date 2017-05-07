#Christopher Snyder
#Student ID: 001178681
#ICSI431 Data Mining
 
 
import tweepy, sys, json, matplotlib.pyplot as plt
from collections import Counter
 
 
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import pylab as pl
import numpy as np
from sklearn import cross_validation
from sklearn.grid_search import GridSearchCV
 
 
#consumer_key = 'uGu4hEOYb2J6mdjWvqn8obtSA'
#consumer_secret = 'eQtvSeyYPy43ThrHnymkj3Nfc5fEAK8gI3eV0JRk3wGUzX6Dcu'
#access_token_key = '742854514957508612-ouGbnSx2IYanANuuoUDLg30dO1mKIn3'
#access_token_secret = 'LgPk2bfdTRXQC7GKfYkdGw2hXrrRMQfcFeqMmvP8WN8Wz'
 
consumer_key='PeH7lROp4ihy4QyK87FZg'
consumer_secret='1BdUkBd9cQK6JcJPll7CkDPbfWEiOyBqqL2KKwT3Og'
access_token_key='1683902912-j3558MXwXJ3uHIuZw8eRfolbEGrzN1zQO6UThc7'
access_token_secret='e286LQQTtkPhzmsEMnq679m7seqH4ofTDqeArDEgtXw'
 
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
myApi = tweepy.API(auth)
 
 
stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
 
 
replacements = [':', '#', ';', '.', ' is ', ' the ', ' you ', ' we ', ' to ',' for ', ' a ', ' la ', ' de ',' and ',' i ',' they ',' of ',' - ', ' en ',
                ' with ', ' on ', ' at ',' by ']
 
#Collect a number of tweets (cnt) based on query
def get_tweets(cnt, query):
    geo = '42.6525,-73.7572,9mi'
    tweets = myApi.search(q=query, count=cnt)
 
    with open("unlabeled_tweets.txt", "a") as outFile:
        for tweet in tweets:
             atts = [tweet.text]
             outFile.write(json.dumps(atts) + "\n")
    print "Tweets successfully collected"
 
 
#Using the tweets collected in the get_tweets() function and store in tweets.txt, this function will
#print out each tweet and allow the user to score it. 0 for neg, 1 for pos. Writes neg and pos
#tweets to their respective files with score added. Also has error handling to make sure score is either 0 or 1
def score_tweets(infile):
    pos = 0
    neg = 0
    for line in open(infile, "r").readlines():
        tweet = json.loads(line)
        score = 2
        while(score != 1 and score != 0):
            try:
                score = int(raw_input(tweet[0]))
                if(score != 1 and score != 0):
                    print "Invalid score. Enter 0 or 1"
            except:
                print "Invalid score. Enter 0 or 1"
       
        out = [score, tweet[0]]
 
        if score == 0:
            neg += 1
            with open("labeled_tweets.txt", "a") as outfile:
                outfile.write(json.dumps(out) +"\n")
           
        elif score == 1:
            pos += 1
            with open("labeled_tweets.txt", "a") as outfile:
                outfile.write(json.dumps(out)+"\n")
        print "neg: ",neg," pos: ",pos
        print("\n")
 
    print "Tweets successfully scored"
 
def calc_freq(filenameL, filenameU):
    tweets = []
    for line in open(filenameL, "r").readlines():
        tweet = json.loads(line)
        tweets.append([tweet[0], tweet[1].lower().strip()])
 
    # Extract the vocabulary of keywords
    vocab = dict()
    for class_label, text in tweets:
        for term in text.split():
            term = term.lower()
            if len(term) > 2 and term not in stopwords:
                if vocab.has_key(term):
                    vocab[term] = vocab[term] + 1
                else:
                    vocab[term] = 1
 
    # Remove terms whose frequencies are less than a threshold (e.g., 15)
    vocab = {term: freq for term, freq in vocab.items() if freq > 15}
    # Generate an id (starting from 0) for each term in vocab
    vocab = {term: idx for idx, (term, freq) in enumerate(vocab.items())}
    print vocab
 
    # Generate X and y
    X = []
    y = []
    for class_label, text in tweets:
        x = [0] * len(vocab)
        terms = [term for term in text.split() if len(term) > 2]
        for term in terms:
            if vocab.has_key(term):
                x[vocab[term]] += 1
        y.append(class_label)
        X.append(x)
 
    # 10 folder cross validation to estimate the best w and b
    svc = svm.SVC(kernel='linear')
    Cs = range(1, 20)
    clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), cv = 10)
    clf.fit(X, y)
 
# predict the class labels of new tweets
    print clf.predict(X)
    tweets = []
    for line in open(filenameU).readlines():
        tweets.append(line)
 
# Generate X for testing tweets
    X = []
    for text in tweets:
        x = [0] * len(vocab)
        terms = [term for term in text.split() if len(term) > 2]
        for term in terms:
            if vocab.has_key(term):
                x[vocab[term]] += 1
        X.append(x)
    y = clf.predict(X)
 
    # print 100 example tweets and their class labels
    for idx in range(1,100):
        print 'Sentiment Class (1 means positive; 0 means negative): ', y[idx]
        print 'TEXT: ', idx, tweets[idx]
 
    print sum(y), len(y)
 
 
def calculate_metrics(queried_file, unqueried_file):
    tweets = []
    for line in open(queried_file, "r").readlines():
        tweet = json.loads(line)
        tweets.append([tweet[0], tweet[1].lower().strip()])
 
    A = 0.0
    B = 0.0
    C = 0.0
    M = 0.0
    N = 0.0
 
    for class_label, text in tweets:
        if class_label == 1:
            A = A + 1
        M = M + 1
        N = N + 1
 
    more_tweets = []
    for line in open(unqueried_file, "r").readlines():
        tweet = json.loads(line)
        more_tweets.append([tweet[0], tweet[1].lower().strip()])
 
    for class_label, text in more_tweets:
        if class_label == 1:
            B = B + 1
        N = N + 1
 
    print "A is:",A
    print "B is:",B
 
    api_recall = M / N
    quality_precision = A / M
    quality_recall = A / (A + B + C)
 
    print "API Recall:",api_recall
    print "Quality Precision:",quality_precision
    print "Quality Recall:",quality_recall
 
if __name__ == '__main__':
   
     #get_tweets(200, "a")
     #score_tweets("unlabeled_tweets.txt")
    calculate_metrics("queried_tweets.txt", "unqueried_tweets.txt")
    #calc_freq("labeled_tweets.txt", "unlabeled_tweets.txt")
