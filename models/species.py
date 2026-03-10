from decimal import Decimal
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class SpeciesBase(SQLModel):
    name: str
    scientific_name: str
    family: str
    conservation_status: str
    wingspan_cm: Decimal

class Species(SpeciesBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # Extra: Allows fetching a species with all its birds
    birds: List["Bird"] = Relationship(back_populates="species")