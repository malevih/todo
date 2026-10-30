from dataclasses import dataclass
from enum import StrEnum

class Check(StrEnum):
    IN_PROGRESS = "in progress"
    DONE = "done"
    ABANDONED = "abandoned"

@dataclass
class TODO:
    name: str
    id:int | None = None
    description: str | None = ""
    state: Check = Check.IN_PROGRESS
