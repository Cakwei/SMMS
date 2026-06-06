from typing import Literal, TypedDict

class TUser(TypedDict):
    userId: int
    username: str
    name: str
    password: str
    role: TRole

TRole = Literal["Admin", "Student", "Lecturer", None]

class TSessionData(TypedDict):
    username: str 
    name: str
    role: TRole

class TReturn(TypedDict):
    success: bool
    message: str
    data: TSessionData | dict
