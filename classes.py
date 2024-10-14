from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field, RootModel
from sqlalchemy.orm import relationship
import enum
from config  import *

Base = declarative_base()

class StatusEnum(str, enum.Enum):
    PLAN = "Планируется"
    IN_PROGRESS = "Выполняется"
    DONE = "Готово"

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.PLAN)

Base.metadata.create_all(bind=create_engine(DATABASE_URL))