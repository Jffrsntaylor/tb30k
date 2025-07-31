"""Status bar showing the turn order."""

from PySide6.QtWidgets import QLabel


class TurnOrderBar(QLabel):
    """Simple label placeholder."""

    def __init__(self) -> None:
        super().__init__("Movement ▶ Shooting ▶ Assault")
