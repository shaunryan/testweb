from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/")
async def read_item(name: str):
    return {"hello": str}

    
