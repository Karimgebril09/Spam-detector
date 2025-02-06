from fastapi import FastAPI,HTTPException
from model import Model
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class Message(BaseModel):
    text:str

@app.post('/predict')
def predict_message(msg: Message) -> dict[str, str]:  
    if len(msg.text) == 0:
        raise HTTPException(status_code=400, detail="Please enter a Message to classify")  # Add 'raise'

    model = Model()
    result = model.predict(msg.text)
    if result == 1:
        return {"prediction": "SPAM"}  # Return a dictionary for consistency
    return {"prediction": "HAM"}  # Return a dictionary for consistency
    