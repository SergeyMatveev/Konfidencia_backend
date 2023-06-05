from fastapi import FastAPI


app = FastAPI(
    title="Konfidencia_backend"
)

@app.get("/")
def get_mainpage():
    return {"message": "Hello, World!"}
