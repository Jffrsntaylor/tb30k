"""Panel for searching rules."""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QListWidget
from Levenshtein import distance


class RuleSearchPanel(QWidget):
    """Simple rule search using Levenshtein distance."""

    rules = {
        "And They Shall Know No Fear": "Unit automatically passes morale tests.",
        "Rending": "Wounds on 6s to hit.",
    }

    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout(self)
        self.edit = QLineEdit()
        self.results = QListWidget()
        layout.addWidget(self.edit)
        layout.addWidget(self.results)
        self.edit.textChanged.connect(self.update_results)

    def update_results(self, text: str) -> None:
        self.results.clear()
        if not text:
            return
        ranked = sorted(self.rules.items(), key=lambda r: distance(text.lower(), r[0].lower()))
        for name, desc in ranked:
            if name.lower().startswith(text.lower()) or distance(text.lower(), name.lower()) < 3:
                self.results.addItem(f"{name}: {desc}")
