from typing import Any, Literal, NotRequired, TypedDict, Optional

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
    data: TSessionData | dict[str, Any]

class TResults(TypedDict):
    resultId: int
    studentId: NotRequired[int | None]
    classId: int
    score: int
    className: NotRequired[str | None]
    semester: NotRequired[int | None]

class TClasses(TypedDict):
    classId: int
    className: str
    semester: int