import sys
import time

from tasker_cli import TaskTable, Task

with TaskTable(
    title="TASK TABLE",
    tasks=[
        Task("Do some stuff"),
        Task("Probably failing stuff"),
        Task("More stuff that is not going to be executed"),
    ],
) as task_table:
    task_table.start_task(0)
    time.sleep(4)
    task_table.end_task(0)

    try:
        task_table.start_task(1)
        time.sleep(4)
        raise ValueError("Something wrong happened!")
        task_table.end_task(1)
    except:
        task_table.end_task(1, result="error")
        sys.exit()

    task_table.start_task(2)
    time.sleep(4)
    task_table.end_task(0)
