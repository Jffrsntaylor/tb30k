"""Splash screen with animated logo."""

from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtCore import Qt, QTimer
from pathlib import Path


class SplashScreen(QSplashScreen):
    """Animated splash screen."""

    def __init__(self) -> None:
        pixmap = QPixmap(str(Path(__file__).resolve().parent.parent / "assets/icons/unit.png"))
        super().__init__(pixmap)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.movie = QMovie(str(Path(__file__).resolve().parent.parent / "assets/icons/unit.png"))
        self.movie.frameChanged.connect(lambda _: self.setPixmap(self.movie.currentPixmap()))
        self.movie.start()
        QTimer.singleShot(1500, self.close)
