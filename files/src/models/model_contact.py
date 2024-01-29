from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class ModelContact(Base):
    """Contact model."""

    __tablename__ = 'contact'

    id = Column('id', Integer)
    name = Column('name', String)
    mail = Column('height', String)
   