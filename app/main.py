from fastapi import FastAPI
from pydantic import BaseModel
from utils import detect_emotion_rule

app = FastAPI()

class InputText(BaseModel):
    sentence: str

@app.post("/predict")
def predict_emotion(data: InputText):
    print("Văn bản nhận được: ", data.sentence)
    return {"emotion": detect_emotion_rule(data.sentence)}

    
