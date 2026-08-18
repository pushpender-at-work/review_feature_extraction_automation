from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import spacy

app=FastAPI(title="Review Feature Extraction")

nlp=spacy.load('en_core_web_en')

class reviewRequest(BaseModel):
    review:str

class bulkreviewRequest(BaseModel):
    reviews:list[str]


def extract_features(text:str):
    doc=nlp(text)
    features=[token.text.lower() for token in doc if token.pos_=='NOUN']
    return features

@app.post('/extract_features')
def get_features(request:reviewRequest):
    if not request.review.strip():
        raise HTTPException(status_code=400,detail="Review text can not be Empty")

    features=extract_features(request.review)
    return {
        'review':request.review,
        'Features':features,
        'feature_count':len(features)
    }


