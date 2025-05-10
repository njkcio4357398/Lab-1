from PyQt6.QtWidgets import QApplication
from gui import VoteApp
import sys

def main() -> None:
    app = QApplication(sys.argv)
    window = VoteApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
