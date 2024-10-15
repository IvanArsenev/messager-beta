from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field, RootModel
from sqlalchemy.orm import relationship
import enum
from typing import Optional
from typing import Dict

from config  import *

Base = declarative_base()

class StatusEnum(str, enum.Enum):
    PLAN = "Планируется"
    IN_PROGRESS = "Выполняется"
    DONE = "Готово"

    @classmethod
    def from_str(cls, status_str: str):
        mapping = {
            "PLAN": cls.PLAN,
            "IN_PROGRESS": cls.IN_PROGRESS,
            "DONE": cls.DONE
        }
        if status_str not in mapping:
            raise ValueError(f"Недопустимый статус: {status_str}")
        return mapping[status_str]

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.PLAN)

class TaskRequest(BaseModel):
    name: str
    description: Optional[str] = Field(None)
    status: Optional[str] = Field(StatusEnum.PLAN)

class StatusUpdateRequest(BaseModel):
    status: str  # Ожидается статус в английском формате

Base.metadata.create_all(bind=create_engine(DATABASE_URL))