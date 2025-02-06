from fastapi import FastAPI,HTTPException
from model import Model
from pydantic import BaseModel

app=FastAPI()

class Message(BaseModel):
    text:str

@app.post('/predict')
def predict_message(msg:Message)->str:
    if len(msg.text)==0:
        HTTPException(status_code=400,detail="Please enter a Message to classify")

    model=Model()
    result=model.predict(msg.text)
    if result == 1:
        return "SPAM"
    return "HAM"
    