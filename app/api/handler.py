from typing import Union
from fastapi import Depends, FastAPI, Request
from pydantic import BaseModel
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from models import errors
import logging
import logger_config
from dependencies import dependencies

logger = logging.getLogger(__name__)
app = FastAPI()

class Item(BaseModel):
    name: str
    price : int

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logger.error("Returning validation error to client")
    errorText=""
    if len(exc.errors()) >0 and "ctx" in exc.errors()[0] and "error" in exc.errors()[0]["ctx"]:
        errorText = str(exc.errors()[0]['ctx']['error'])
    return JSONResponse(
        status_code=400,
        content={"message": f"Validation Error: {errorText}"},
    )

@app.exception_handler(errors.DatabaseException)
async def database_exception_handler(request: Request, exc: errors.DatabaseException):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Database Error"},
    )

@app.get("/")
def read_root(): # only use async if your code uses it
    logger.info("Reading root")
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    logger.info("Reading item")
    return {"item_id": item_id, "q": q}

@app.post("/items/", status_code=201)
async def create_item(item: Item):
    logger.info("Creating item")
    dependencies.createService.create_item(item.name,item.price)
    logger.info("Item created")
    return {"name": item.name}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    logger.info("Updating item")
    return {"item_name": item.name, "item_id": item_id}