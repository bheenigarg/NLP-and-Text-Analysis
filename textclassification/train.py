# Step 1-- Build a model

import pandas as pd

# load the data
df = pd.read_csv('train.csv')

# divide columns into training and response
X_train = df['tweet']
y_train = df['label']

from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier

# create pipeline to train model on raw data
pipeline = make_pipeline(CountVectorizer(ngram_range=(1, 2)), TfidfTransformer(), SGDClassifier(loss='hinge'))

model = pipeline.fit(X_train, y_train)

# input raw data
test_tweet = ['#studiolife #aislife #requires #passion #dedication #willpower   to find #newmaterials', ' @user #white #supremacists want everyone to see the new   #birds#movie and heres why  ', 'safe ways to heal your #acne!!    #altwaystoheal #healthy   #healing!! ']

# predict the classes
predictions = pipeline.predict(test_tweet)

# Print the outputs
for tweet, label in zip(test_tweet, predictions):
    print('\nTweet: {} \nPredicted label: {}'.format(tweet, label))


# Step 2 -- Saving the model using Pickle

import pickle

with open('model.pkl', 'wb') as fid:
    pickle.dump(pipeline, fid)
