from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "world"}

@app.get("/test")
def hello1():
    return {"test": "test"}
