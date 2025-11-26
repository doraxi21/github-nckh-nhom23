from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputText(BaseModel):
    sentence: str

@app.post("/predict")
def predict_emotion(data: InputText):
    print("Văn bản nhận được: ", data.sentence)
    return {"message": f"Bạn vừa gửi: {data.sentence}"}
