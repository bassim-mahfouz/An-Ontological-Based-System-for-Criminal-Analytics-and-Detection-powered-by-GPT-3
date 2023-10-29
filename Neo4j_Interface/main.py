from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import Dict
from pydantic import BaseModel
from Services import InfoExtractor

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    )

class Data(BaseModel):
    prompt:str

@app.get('/endpoint')
async def get_resource():
    # response = service.chat_with_gpt("hello")
    return {"data": "hello"}

@app.post('/integrate/')
async def post_resource(data: Data):
    if data.get('path') :
        value= StructuredDataMapper.integrate_csv_files_from_directory(data.get('path'))
    return {'response': "sucess"}

@app.post('/answer')
async def post_resource(data: Data):
    if data.prompt :
        value=InfoExtractor.extractKnowledge(data.prompt)
    return {'response': value}