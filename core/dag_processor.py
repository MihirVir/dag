from functools import wraps 
from datetime import datetime 
from . import tasks

class Dag():
    def __init__(self, name: str,dag_id: str, tags: list=[], start_date: datetime=datetime.now(), scheduled_interval: str|None=None):
        self.name = name
        self.dag_id = dag_id
        self.tags = tags 
        self.start_date= start_date
        self.scheduled_interval = scheduled_interval
        self.tasks = tasks.Tasks() 

    def create_task(self, task_id: str, cb: callable): 
        self.tasks.add_tasks(dag_id=self.dag_id,task_id=task_id, cb=cb)
    
    def run(self):
        print(f"Running DAG: {self.dag_id}")

        for task in self.tasks.get_tasks(self.dag_id):
            print(f"running task {task["task_id"]}")
            task["cb"]()


def dag(start_date=None, scheduled_interval=None, dag_id=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            dag_obj = Dag(
                name=func.__name__, 
                start_date=start_date,
                dag_id=dag_id,
                tags=[],
                scheduled_interval=scheduled_interval
            )

            func(dag_obj, *args, **kwargs)

            return dag_obj
        return wrapper
    return decorator

