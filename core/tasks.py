from collections import defaultdict

class Tasks: 
    def __init__(self):
        self.tasks = defaultdict(list)
    
    def add_tasks(self, dag_id: str, task_id: str, cb: callable): 
        self.tasks[dag_id].append({"task_id": task_id,"cb": cb})
    
    def get_tasks(self, dag_id: str) -> list:
        return self.tasks[dag_id]