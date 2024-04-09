from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import sqlite_utils

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')

# SQLite 데이터베이스 연결
db = sqlite_utils.Database("/data/data.db")

# Pydantic을 사용하여 모델 정의
class Item(BaseModel):
    name: str
    description: str = None

# 데이터베이스에 존재하는 모든 아이템을 반환하는 엔드포인트
@app.get("/api/items/", response_model=List[Item])
async def read_items():
    items = db["items"].rows
    return items

# 데이터베이스에 새로운 아이템을 추가하는 엔드포인트
@app.post("/api/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    db["items"].insert(item_dict)
    return item_dict
