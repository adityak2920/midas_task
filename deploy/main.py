import joblib
import praw
from fastapi import FastAPI, Query, File, UploadFile
import uvicorn
from pydantic import BaseModel


reddit = praw.Reddit(client_id='NJdBzvaaUnVwQg', client_secret='z2nWItCDkMHYhl2NcXbpRs30yO0', user_agent='reddit scrap')

flairs = ['AskIndia', 'Business/Finance', 'Coronavirus', 'Non-Political', 'Policy/Economy', 'Politics', 'Science/Technology']


app = FastAPI()


def get_text(url_list):
     title_list = []
     for j in url_list:
         submission = reddit.submission(url=j)
         text = submission.title
         title_list.append(text)
     return title_list


def get_itext(link):
    submission = reddit.submission(url=link)
    text = submission.title
    return text


def prediction(text_list):
    if type(text_list) is not list:
        text_list = [text_list]
    vector = tf_idf.transform(text_list)
    predictions = model.predict(vector)
    result = [flairs[i] for i in predictions]
    return result
    

tf_idf = joblib.load("tfidf_vectors.sav")
model = joblib.load("lgr_tfidf.sav")

class Item(BaseModel):
    name: str


@app.post("/predict")
async def predict_link(item: Item):
    print(item)
    text = get_itext(item.dict()["name"])
    predict = prediction(text)
    return predict

@app.post("/predict_file")
async def predict_file(file: UploadFile = File(...)):
    contents = await file.read()
    contents = contents.decode("utf-8")
    links = list(contents.split("\n"))
    title_list = get_text(links[:-1])
    result = prediction(title_list)
    return {"result":result}




