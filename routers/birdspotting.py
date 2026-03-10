from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models.birdspotting import Birdspotting, BirdspottingCreate
from repositories.birdspotting import BirdspottingRepository

router = APIRouter(prefix="/birdspotting", tags=["Birdspotting"])

def get_repo(session: Annotated[Session, Depends(get_session)]):
    return BirdspottingRepository(session)

@router.get("/", response_model=List[Birdspotting])
async def read_all(repo: Annotated[BirdspottingRepository, Depends(get_repo)]):
    return repo.get_all()

@router.get("/{id}", response_model=Birdspotting)
async def read_one(id: int, repo: Annotated[BirdspottingRepository, Depends(get_repo)]):
    item = repo.get_one(id)
    if not item:
        raise HTTPException(status_code=404, detail="Observation not found")
    return item

@router.post("/", response_model=Birdspotting, status_code=201)
async def create(payload: BirdspottingCreate, repo: Annotated[BirdspottingRepository, Depends(get_repo)]):
    return repo.insert(payload)