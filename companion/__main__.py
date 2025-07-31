"""Command line entry point for the Warhammer Companion application."""

from PySide6.QtWidgets import QApplication
from .gui.splash import SplashScreen
from .gui.main_window import MainWindow
import sys


def main() -> None:
    """Launch the application."""
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    app.processEvents()
    window = MainWindow()
    splash.finish(window)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
