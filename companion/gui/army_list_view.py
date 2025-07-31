"""Widget showing the current army list."""

from PySide6.QtWidgets import QListWidget


class ArmyListView(QListWidget):
    """Simple list widget placeholder."""

    def __init__(self) -> None:
        super().__init__()
        self.addItem("Tactical Squad - 100 pts")
