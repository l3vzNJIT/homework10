from builtins import ValueError, any, bool, str
from pydantic import BaseModel, EmailStr, Field, validator, root_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum
import uuid
import re

from app.utils.nickname_gen import generate_nickname

# Shared example user (for /docs example values)
example_user = {
    "email": "jane.doe@example.com",
    "password": "Secure*1234",
    "nickname": "jane_dev123",
    "first_name": "Jane",
    "last_name": "Doe",
    "bio": "Senior backend engineer passionate about Python and FastAPI.",
    "profile_picture_url": "https://example.com/profiles/jane.jpg",
    "linkedin_profile_url": "https://linkedin.com/in/janedoe",
    "github_profile_url": "https://github.com/janedoe",
    "id": "123e4567-e89b-12d3-a456-426614174000"
}

class UserRole(str, Enum):
    ANONYMOUS = "ANONYMOUS"
    AUTHENTICATED = "AUTHENTICATED"
    MANAGER = "MANAGER"
    ADMIN = "ADMIN"

def validate_url(url: Optional[str]) -> Optional[str]:
    if url is None:
        return url
    url_regex = r'^https?:\/\/[\S]+$'
    if not re.match(url_regex, url):
        raise ValueError('Invalid URL format')
    return url

class UserBase(BaseModel):
    email: EmailStr = Field(..., example=example_user["email"])
    nickname: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example=example_user["nickname"])
    first_name: Optional[str] = Field(None, example=example_user["first_name"])
    last_name: Optional[str] = Field(None, example=example_user["last_name"])
    bio: Optional[str] = Field(None, example=example_user["bio"])
    profile_picture_url: Optional[str] = Field(None, example=example_user["profile_picture_url"])
    linkedin_profile_url: Optional[str] = Field(None, example=example_user["linkedin_profile_url"])
    github_profile_url: Optional[str] = Field(None, example=example_user["github_profile_url"])

    _validate_urls = validator('profile_picture_url', 'linkedin_profile_url', 'github_profile_url', pre=True, allow_reuse=True)(validate_url)

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    email: EmailStr = Field(..., example=example_user["email"])
    password: str = Field(..., example=example_user["password"])

class UserUpdate(UserBase):
    email: Optional[EmailStr] = Field(None, example=example_user["email"])
    nickname: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example=example_user["nickname"])
    first_name: Optional[str] = Field(None, example=example_user["first_name"])
    last_name: Optional[str] = Field(None, example=example_user["last_name"])
    bio: Optional[str] = Field(None, example=example_user["bio"])
    profile_picture_url: Optional[str] = Field(None, example=example_user["profile_picture_url"])
    linkedin_profile_url: Optional[str] = Field(None, example=example_user["linkedin_profile_url"])
    github_profile_url: Optional[str] = Field(None, example=example_user["github_profile_url"])

    @root_validator(pre=True)
    def check_at_least_one_value(cls, values):
        if not any(values.values()):
            raise ValueError("At least one field must be provided for update")
        return values

class UserResponse(UserBase):
    id: uuid.UUID = Field(..., example=example_user["id"])
    role: UserRole = Field(default=UserRole.AUTHENTICATED, example="AUTHENTICATED")
    email: EmailStr = Field(..., example=example_user["email"])
    nickname: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example=example_user["nickname"])
    is_professional: Optional[bool] = Field(default=False, example=True)

class LoginRequest(BaseModel):
    email: str = Field(..., example=example_user["email"])
    password: str = Field(..., example=example_user["password"])

class ErrorResponse(BaseModel):
    error: str = Field(..., example="Not Found")
    details: Optional[str] = Field(None, example="The requested resource was not found.")

class UserListResponse(BaseModel):
    items: List[UserResponse] = Field(..., example=[{
        "id": example_user["id"],
        "nickname": example_user["nickname"],
        "email": example_user["email"],
        "first_name": example_user["first_name"],
        "last_name": example_user["last_name"],
        "bio": example_user["bio"],
        "role": "AUTHENTICATED",
        "profile_picture_url": example_user["profile_picture_url"],
        "linkedin_profile_url": example_user["linkedin_profile_url"],
        "github_profile_url": example_user["github_profile_url"]
    }])
    total: int = Field(..., example=100)
    page: int = Field(..., example=1)
    size: int = Field(..., example=10)
