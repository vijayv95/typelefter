from PySide6.QtWidgets import QApplication, QMainWindow
import sys

def run_app():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Typelefter")
    window.show()
    sys.exit(app.exec())
