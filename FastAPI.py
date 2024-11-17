from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)


class SearchRequest(BaseModel):
    user_id: str
    query: str
    filters: dict


@app.post("/search")
def search_data(request: SearchRequest):

    data = {"results": ["Artigo 1", "Artigo 2", "Artigo 3"]}
    return {"query": request.query, "filters": request.filters, "results": data}
