"""Main application window."""

from PySide6.QtWidgets import (
    QMainWindow,
    QSplitter,
    QWidget,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtCore import Qt

from .faction_unit_tree import FactionUnitTree
from .army_list_view import ArmyListView
from .unit_detail_panel import UnitDetailPanel
from .rule_search_panel import RuleSearchPanel
from .turn_order_bar import TurnOrderBar


class MainWindow(QMainWindow):
    """Main application window with split layout."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Warhammer Companion")
        self.resize(1024, 768)

        splitter = QSplitter(Qt.Horizontal)

        self.tree = FactionUnitTree()
        self.list_view = ArmyListView()
        self.detail = UnitDetailPanel()
        self.search = RuleSearchPanel()
        self.turn_bar = TurnOrderBar()

        splitter.addWidget(self.tree)
        splitter.addWidget(self.list_view)

        right = QSplitter(Qt.Vertical)
        right.addWidget(self.detail)
        right.addWidget(self.search)
        splitter.addWidget(right)

        central = QWidget()
        layout = QVBoxLayout(central)
        layout.addWidget(splitter)
        layout.addWidget(self.turn_bar)
        self.setCentralWidget(central)
