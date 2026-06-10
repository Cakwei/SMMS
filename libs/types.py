from typing import Literal, NotRequired, TypedDict, Optional

TRole = Literal["Admin", "Student", "Lecturer", None]

class TUser(TypedDict):
    lecturerId: NotRequired[int]
    adminId: NotRequired[int]
    studentId: NotRequired[int]
    username: str
    name: str
    password: str
    role: TRole

class TSessionData(TypedDict):
    id: str
    username: str 
    name: str
    role: TRole

class TReturn(TypedDict):
    success: bool
    message: str
    data: TSessionData | dict

class TResults(TypedDict):
    resultId: int
    studentId: int
    classId: int
    score: int