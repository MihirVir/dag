import uuid 
from enum import Enum
from typing import Dict, Callable, Optional, Set 

class TaskState(Enum):
    IDLE = "IDLE"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

class Task:
    def __init__(self, task_id: str, cb: Callable, retries: int=3):
        self.task_id = task_id
        self.cb = cb 
        self.retries = retries
        self.state: Dict[str, TaskState] = {} # run_id: task state
        self.next: Optional["Task"] = None 

    def __rshift__(self, task: "Task") -> "Task":
        self.next = task
        return task

    def run(self, run_id: str) -> None: 
        self.state[run_id] = TaskState.PENDING
        attempt = 0 

        while attempt < self.retries:
            try: 
                self.cb()
                self.state[run_id] = TaskState.SUCCESS
                break
            except Exception as e: 
                attempt += 1
                print(f"[Task {self.task_id}] Attempt {attempt} failed: {e}")
                if attempt == self.retries:
                    self.state[run_id] = TaskState.FAILURE
    
