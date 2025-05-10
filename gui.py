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

        # Add voting buttons
        for name, button in self.buttons.items():
            layout.addWidget(button)
            button.clicked.connect(lambda _, n=name: self.cast_vote(n))

        # Add Reset button
        self.reset_button = QPushButton("Reset Votes")
        self.reset_button.clicked.connect(self.reset_votes)
        layout.addWidget(self.reset_button)

        self.setLayout(layout)

    def cast_vote(self, name: str) -> None:
        """Handle voting logic."""
        if self.tracker.vote(name):
            QMessageBox.information(self, "Vote Submitted", f"Thank you for voting for {name}!")
        else:
            QMessageBox.warning(self, "Error", "Invalid candidate.")

    def reset_votes(self) -> None:
        """Reset all votes to zero."""
        self.tracker.reset()
        QMessageBox.information(self, "Reset Complete", "All votes have been reset to 0.")

    def closeEvent(self, event) -> None:
        """Show final vote summary and save votes on close."""
        results = self.tracker.get_results()
        total_votes = sum(results.values())
        message = "\n".join(f"{name}: {count} votes" for name, count in results.items())
        message += f"\n\nGrand Total: {total_votes} votes"

        QMessageBox.information(self, "Final Vote Results", message)
        save_votes_to_csv(results)
        event.accept()
