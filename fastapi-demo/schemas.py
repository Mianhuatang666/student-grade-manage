from pydantic import BaseModel, Field, field_validator


class Student(BaseModel):
    name: str = Field(min_length=1)
    score: int = Field(ge=0, le=100)

    @field_validator("name")
    @classmethod
    def check_name(cls, value):
        value = value.strip()

        if value == "":
            raise ValueError("姓名不能为空")

        return value


class UpdateScore(BaseModel):
    score: int = Field(ge=0, le=100)

class UserRegister(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=6)

    @field_validator("username")
    @classmethod
    def check_username(cls, value):
        value = value.strip()

        if value == "":
            raise ValueError("用户名不能为空")

        return value

class UserLogin(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=6)

    @field_validator("username")
    @classmethod
    def check_username(cls, value):
        value = value.strip()

        if value == "":
            raise ValueError("用户名不能为空")

        return value

class TokenResponse(BaseModel):
    access_token: str
    token_type: str