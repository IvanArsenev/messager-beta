from fastapi import FastAPI
app = FastAPI()

@app.get("/test")
async def get_test():
    return {"message": "OK"}

@app.post("/test/{id}")
async def post_test(id: int):
    return {"message": id}