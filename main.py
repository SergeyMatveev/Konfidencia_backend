from fastapi import FastAPI

app = FastAPI()


@app.get("/{item}")
def hello(item=int):
    t = item
    return "Hello world!" + t
