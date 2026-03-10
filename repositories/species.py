from sqlmodel import Session, select
from models.species import Species

class SpeciesRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_all(self):
        return self.session.exec(select(Species)).all()