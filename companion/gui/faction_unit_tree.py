"""Tree widget listing factions and units."""

from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem


class FactionUnitTree(QTreeWidget):
    """Simple tree for demo purposes."""

    def __init__(self) -> None:
        super().__init__()
        self.setHeaderHidden(True)
        faction = QTreeWidgetItem(["Demo Faction"])
        unit = QTreeWidgetItem(["Tactical Squad"])
        faction.addChild(unit)
        self.addTopLevelItem(faction)
