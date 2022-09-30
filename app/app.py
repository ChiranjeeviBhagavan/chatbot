# main.py
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from Recommendation_Generator.generator import recommendationGenerator
from predict import chattyAnswer

PROJECT_PATH = r"C:\Users\Administrator\chatbot\app\Courses-Recommendation-system"
DATA_PATH = r"C:\Users\Administrator\chatbot\app\data\features_sample.csv"

app = FastAPI()

features,data = recommendationGenerator.load_data(recommendationGenerator, datapath= DATA_PATH)
class Item(BaseModel):
    id : str
    q: Optional[str]
    a: Optional[str]


@app.post("/chat")
async def chatty(d : Item):
    model = recommendationGenerator(163036, 4)
    recomm = model.generate_recommendations(features, data)
    id = d.id
    id = 163036
    d.a = chattyAnswer(d.q)
    if "{##$##}" in d.a:
        model = recommendationGenerator(163036, 4)
        recomm = model.generate_recommendations(features, data)
        print(recomm)
        d.a = d.a.replace("{##$##}"," ".join(recomm))

    #d.dict()["a"] = ".".join(map(str,recomm))
    #print(recomm)
    return d