"""Dialog for editing JSON data files."""

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel


class DataEditor(QDialog):
    """Placeholder editor dialog."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Data Editor")
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Data editor not implemented."))
