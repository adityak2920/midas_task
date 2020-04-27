# importing libraries
import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
import flask
import praw
import joblib

# difining app
app = Flask(__name__)

# initialising praw with credentials for fetching posts
reddit = praw.Reddit(client_id='NJdBzvaaUnVwQg', client_secret='z2nWItCDkMHYhl2NcXbpRs30yO0', user_agent='reddit scrap')

# declairing name of flairs
flairs = ['AskIndia', 'Business/Finance', 'Coronavirus', 'Non-Political',
 'Policy/Economy', 'Politics', 'Science/Technology']

# defining the tokenization function fro count vectors
# def wordtokenize(text):
#     tokens = word_tokenize(text)
#     stems = []
#     for item in tokens:
#         stems.append(PorterStemmer().stem(item))
#     return stems

# loading weights of vectors and classifier
count_model = joblib.load("count_vectors.sav")
lgr_model = joblib.load("lgr_count.sav")


# function to fetch text of post from the url
def get_text(url_list):
    title_list = []
    for j in url_list:
        submission = reddit.submission(url=j)
        text = submission.title
        title_list.append(text)
    return title_list

# function for predicting flair for the post
def prediction(text_list):
    vector = count_model.transform(text_list)
    predictions = lgr_model.predict(vector)
    result = [flairs[i] for i in predictions]
    return result



# creating the flask app function
DIR= "temp"
@app.route("/automated_testing", methods=['POST'])
def hello():
    if not os.path.exists(DIR):
        os.mkdir(DIR)
    f = request.files['upload_file']
    filename = f.filename
    f.save("{}/{}".format(DIR,filename))
    with open("{}/{}".format(DIR, filename),'r') as file:
        file_data = file.read()
        links = list(file_data.split("\n"))
        title_list = get_text(links[:-1])
        result = prediction(title_list)
        return {"result":result}


if __name__ == "__main__":
 # running the app
     app.run(host='0.0.0.0', debug=True)
