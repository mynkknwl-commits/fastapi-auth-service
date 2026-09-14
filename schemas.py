from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date, datetime
from typing import Optional

# ---------- User ---------- 
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# ---------- Application ----------
class ApplicationCreate(BaseModel):
    company: str
    role: str
    status: str = "applied"
    applied_date: date
    follow_up_date: Optional[date] = None
    notes: Optional[str] = None

class ApplicationUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None
    applied_date: Optional[date] = None
    follow_up_date: Optional[date] = None
    notes: Optional[str] = None

class ApplicationOut(BaseModel):
    id: int
    company: str
    role: str
    status: str
    applied_date: date
    follow_up_date: Optional[date]
    notes: Optional[str]

    model_config = ConfigDict(from_attributes=True)