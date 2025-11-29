from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "KB Range Management System API is running!"}


@app.get("/status")
def status():
    return {
        "system": "KB Range Management System",
        "status": "online",
        "version": "0.1.0"
    }
