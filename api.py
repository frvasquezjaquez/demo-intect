from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Pide un nombre"}

@app.get("/fv")
async def root():
    return {"myName": "Francisco Vasquez"}

@app.get("/vc")
async def root():
    return {"myName": "Victor Calderón"}

@app.get("/jg")
async def root():
    return {"myName": "Jeffrey Grassals"} 