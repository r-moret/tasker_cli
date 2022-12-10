from tasker_cli import TaskTable, Task
import time

with TaskTable(
    title="TASK TABLE", 
    tasks=[
        Task("Do some stuff"), 
        Task("And then more boring stuff"),
    ],
) as task_table:
    task_table.start_task(0)
    time.sleep(4)
    task_table.end_task(0)

    task_table.start_task(1)
    time.sleep(4)
    task_table.end_task(1)
