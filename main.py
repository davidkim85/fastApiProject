from fastapi import FastAPI
from os import environ as env
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name} David Shlomi {env['MY_VARIABLE']}"}
