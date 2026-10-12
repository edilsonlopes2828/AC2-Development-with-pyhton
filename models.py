
from sqlalchemy import Column, Integer, String
from database import Base


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    seasons = Column(Integer, nullable=False)

    def __repr__(self):
        return (
            f"Series(id={self.id}, title='{self.title}', "
            f"genre='{self.genre}', seasons={self.seasons})"
        )
