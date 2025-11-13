from typing import Union
from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def printsomething():
    print("Server is on")