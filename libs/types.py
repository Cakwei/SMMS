from typing import NotRequired, TypedDict

class TAdmins(TypedDict):
    userId: int
    username: str
    password: str
    role: str

class TSessionData(TypedDict):
    username: str
    role: str

class TReturn(TypedDict):
    success: bool
    message: str
    data: TSessionData | dict

