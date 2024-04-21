from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
    
    email: EmailStr
    password: str = Field(max_length=255)
    
    
class UserLinkedinCredentials(BaseModel):
    
    email_login: EmailStr
    password_login: str = Field(max_length=255)
    
    