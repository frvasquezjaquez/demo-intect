from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Pide un nombre"}

@app.get("/fv")
async def root():
    return {"myName": "Francisco Vasquez"}

@app.get("/fc")
async def root():
    return {"myName": "Fernando Cabrera"}


