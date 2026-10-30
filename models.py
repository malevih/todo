from dataclasses import dataclass
from enum import StrEnum

class TaskStatus(StrEnum):
    IN_PROGRESS = "in progress"
    DONE = "done"
    ABANDONED = "abandoned"

@dataclass
class Task:
    name: str
    id:int | None = None
    description: str | None = None
    state: TaskStatus = TaskStatus.IN_PROGRESS

    def __str__(self):
        return f"{self.id}: [{self.name}] {self.description} -> {self.state}"
