from rich.align import Align
from rich.box import HEAVY_HEAD
from rich.layout import Layout
from rich.live import Live
from rich.padding import Padding
from rich.panel import Panel
from rich.status import Status
from rich.table import Table
from .task import Task


class TaskTable:
    STATUS = {
        "PENDING": "PENDING",
        "ON_PROGRESS": Status("[yellow]ON PROGRESS", spinner_style="yellow"),
        "COMPLETE": "[green]COMPLETE",
        "ERROR": "[red]ERROR",
    }

    def __init__(self, title: str, tasks: list[Task]) -> None:
        table = Table(show_lines=True, show_edge=False, box=HEAVY_HEAD)
        layout = Layout(
            Align.center(
                Padding(
                    Panel(table, title=title, padding=(1, 1, 0, 1)), pad=(2, 0)
                )
            )
        )

        table.add_column("STATUS", justify="center", width=20)
        table.add_column("TASK", justify="center", width=40)

        for task in tasks:
            table.add_row(TaskTable.STATUS["PENDING"], task.title)

        self.layout = layout
        self.table = table
        self.live = None

    def start_task(self, index: int):
        self.table.columns[0]._cells[index] = TaskTable.STATUS["ON_PROGRESS"]

    def end_task(self, index: int, result: str = "complete"):
        RESULTS = {
            "complete": TaskTable.STATUS["COMPLETE"],
            "error": TaskTable.STATUS["ERROR"],
        }

        if result not in RESULTS:
            raise ValueError(
                f"Unknown result status for terminating task {index}"
            )

        self.table.columns[0]._cells[index] = RESULTS[result]

    def __enter__(self):
        self.live = Live(self.layout, refresh_per_second=12.5)
        self.live.__enter__()
        return self

    def __exit__(self, *args, **kwargs):
        self.live.__exit__(*args, **kwargs)
