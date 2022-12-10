class Task:
    def __init__(self, title: str, subtasks: list[str] | None = None) -> None:
        self.title = title
        self.subtasks = subtasks
