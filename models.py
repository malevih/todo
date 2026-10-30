from enum import Enum

class Check(Enum):
    IN_PROGRESS = 1
    DONE = 2
    ABANDONED = 3

class TODO:
    id:int | None = None
    name: str = ""
    state: Check = Check.IN_PROGRESS
