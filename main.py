from fastapi import FastAPI

app = FastAPI()


@app.get("/{item}")
def hello(item=int):
    t = item
    return "Hello world!" + t

#git config --global user.email "you@example.com" git config --global user.name "Sergey Matveev"