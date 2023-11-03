from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi.middleware.cors import CORSMiddleware


origins = ["*"]


app = FastAPI(title = 'Seul Bike Rented Prediction')

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"]
)
model = load(pathlib.Path('model/train.joblib'))

class InputData(BaseModel):
    Date: int = 1122017
    Hour: int = 0
    Temperature: float = -5.2
    Humidity: float = 37
    Wind_Speed: float = 2.2
    Visibility: float = 2000
    Dew_Point: float = -17.6
    Solar_Radiation: float = 0.0
    Rainfall: float = 0.0
    Snowfall: float = 0.0
    Season: int = 1
    IsHoliday: int = 0
    IsFunctioningDay: int = 1

class OutputData(BaseModel):
     Bikes_Rented: int = 254

@app.post('/rented', response_model = OutputData)
def rented(data:InputData):
    model_input = np.array([v for k,v in data.dict().items()]).reshape(1,-1)
    result = model.predict(model_input)

    return {'Bikes_Rented':result}