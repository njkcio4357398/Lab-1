from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
)
from logic import VoteTracker
from storage import save_votes_to_csv

class VoteApp(QWidget):
    """Main window for the voting application."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vote for a Candidate")
        self.tracker = VoteTracker()

        self.label = QLabel("Choose a candidate to vote for:")
        self.buttons = {
            name: QPushButton(f"Vote for {name}") for name in self.tracker.get_results()
        }

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        for name, button in self.buttons.items():
            layout.addWidget(button)
            button.clicked.connect(lambda _, n=name: self.cast_vote(n))

        self.setLayout(layout)

    def cast_vote(self, name: str) -> None:
        """Handle voting logic."""
        if self.tracker.vote(name):
            QMessageBox.information(self, "Vote Submitted", f"Thank you for voting for {name}!")
        else:
            QMessageBox.warning(self, "Error", "Invalid candidate.")

    def closeEvent(self, event) -> None:
        """Save votes on close."""
        save_votes_to_csv(self.tracker.get_results())
        event.accept()
