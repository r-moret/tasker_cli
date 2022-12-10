import time

from tasker_cli import Task, TaskTable

with TaskTable(
    title="TASK TABLE",
    tasks=[
        Task(
            "Install software A",
            subtasks=[
                "Updating repository",
                "Starting installation",
                "Ending configuration",
            ],
        ),
        Task(
            "And then more configuration",
            subtasks=[
                "Configuring additional files",
                "Removing temporary files",
                "Stopping executions of unnecessary processes",
            ],
        ),
    ],
) as task_table:
    task_table.start_task(0)
    time.sleep(4)
    task_table.advance_task(0, 1)
    time.sleep(2)
    task_table.advance_task(0, 2)
    time.sleep(3)
    task_table.end_task(0)

    task_table.start_task(1)
    time.sleep(4)
    task_table.advance_task(1, 1)
    time.sleep(4)
    task_table.advance_task(1, 2)
    time.sleep(4)
    task_table.end_task(1)
