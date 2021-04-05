from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/testendpoint")
async def testendpoint():
    return "YOOOOO this actually works"    