"""Panel showing unit details."""

from PySide6.QtWidgets import QTextEdit


class UnitDetailPanel(QTextEdit):
    """Read-only text area for unit details."""

    def __init__(self) -> None:
        super().__init__()
        self.setReadOnly(True)
        self.setText("Unit details appear here.")
