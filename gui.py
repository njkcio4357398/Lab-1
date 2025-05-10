
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QComboBox
)
from logic import VoteManager


class VotingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voting App")
        self.vote_manager = VoteManager()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Select a candidate to vote:")
        layout.addWidget(self.label)

        self.combo_box = QComboBox()
        self.combo_box.addItems(["", "Bianca", "Edward", "Felicia"])
        layout.addWidget(self.combo_box)

        self.vote_button = QPushButton("Vote")
        self.vote_button.clicked.connect(self.cast_vote)
        layout.addWidget(self.vote_button)

        self.results_button = QPushButton("Show Results")
        self.results_button.clicked.connect(self.show_results)
        layout.addWidget(self.results_button)

        self.setLayout(layout)

    def cast_vote(self):
        candidate = self.combo_box.currentText()
        if candidate == "":
            QMessageBox.warning(self, "Invalid Input", "Please select a candidate.")
            return
        try:
            self.vote_manager.add_vote(candidate)
            QMessageBox.information(self, "Success", f"Voted for {candidate}.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show_results(self):
        try:
            results = self.vote_manager.get_results()
            message = "\n".join(f"{name}: {count} votes" for name, count in results.items())
            total = sum(results.values())
            message += f"\nTotal Votes: {total}"
            QMessageBox.information(self, "Voting Results", message)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


