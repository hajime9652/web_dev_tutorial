from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root_get():
    return {"message": "GET: Read a data"}

@app.post("/")
async def root_post():
    return {"message": "POST: Create a data"}

@app.put("/")
async def root_put():
    return {"message": "PUT Update the data"}

@app.delete("/")
async def root_delete():
    return {"message": "DELETE: Delete the data"}


