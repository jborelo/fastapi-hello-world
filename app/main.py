import uvicorn
from uvicorn.config import Config
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI - Hello World",
    description="This is the Hello World of FastAPI.",
    version="1.0.0",
) 


@app.get("/")
def hello_world():
    return {"Hello": "World"}


if __name__ == "__main__":
    if __name__ == "__main__":
        port = 8000
        print(f"Starting GONZO service on port {port}")
        uvicorn.Server(config=(
            Config(app=app,
                   port=port,
                   host='0.0.0.0',
                   reload=False)
        )).run()

