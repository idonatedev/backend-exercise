from fastapi import FastAPI

app: FastAPI = FastAPI(title="iDonate Backend API")


@app.get("/hello")
def hello(
        name: str = "World",
):
    return f"Hello {name}!"
