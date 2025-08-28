from core.tasks import Task, TaskState
from core.workflow import Workflow

def task_a_fn():
    print("Executing Task A")

def task_b_fn():
    print("Executing Task B")

def task_c_fn():
    print("Executing Task C")

# Create workflow
wf = Workflow("LinkedListWorkflow")

# Create tasks
t1 = Task("A", task_a_fn)
t2 = Task("B", task_b_fn)
t3 = Task("C", task_c_fn)

# Add tasks to workflow
wf.add_task(t1)
wf.add_task(t2)
wf.add_task(t3)

# Chain tasks
t1 >> t2 >> t3

# Run workflow
wf.run()
