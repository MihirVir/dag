from core.tasks import Task, TaskState
from typing import Dict, List, Optional
import uuid 

# TODO: improve syntax for Python DSL
class Workflow:
    def __init__(self, workflow_id: str): 
        self.workflow_id = workflow_id
        self._tasks: List[Task] = []
        self.head: Optional[Task] = None 
    
    def add_task(self, task: Task) -> None:
        self._tasks.append(task)
    
    def _find_head(self):
        referenced = {t.next for t in self._tasks if t.next}
        heads = [t for t in self._tasks if t not in referenced]

        self.head = heads[0] if heads else None 
    
    def detect_circular_dependency(self) -> bool: 
        slow = self.head 
        fast = self.head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast: 
                return True 
        
        return False 

    def run(self) -> None: 
        self._find_head()

        if not self.head:
            Exception("No head task found, can't run workflow")
        
        run_id = str(uuid.uuid4())
        print(f"\n=== Running Workflow '{self.workflow_id}' (Run ID: {run_id}) ===")

        if self.detect_circular_dependency():
            raise Exception("Circular Dependency found! aborting execution")

        current = self.head 

        while current: 
            current.run(run_id=run_id)

            if current.state[run_id] != TaskState.SUCCESS: 
                print(f"[Workflow] Task {current.task_id} failed. Stopping execution")
                break 
                
            current = current.next 
        
        print(f"=== Workflow '{self.workflow_id}' completed ===\n")