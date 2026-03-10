from fastapi import FastAPI
from database import start_db
from routers.species import router as species_router
from routers.birds import router as birds_router
from routers.birdspotting import router as spotting_router

app = FastAPI()
app.include_router(species_router)
app.include_router(birds_router)
app.include_router(spotting_router)


start_db() 

@app.get("/")
async def root():
    return {"message": "Hello World"}