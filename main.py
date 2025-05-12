import os

from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnBottomHint | Qt.WindowType.FramelessWindowHint)

if __name__ == "__main__":
    if os.name == "posix":
        os.environ["QT_QPA_PLATFORM"] = "xcb"

    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec()
