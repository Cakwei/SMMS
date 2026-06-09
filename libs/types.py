from typing import Literal, TypedDict

TRole = Literal["Admin", "Student", "Lecturer", None]

class TUser(TypedDict):
    userId: int
    username: str
    name: str
    password: str
    role: TRole

class TSessionData(TypedDict):
    username: str 
    name: str
    role: TRole

class TReturn(TypedDict):
    success: bool
    message: str
    data: TSessionData | dict