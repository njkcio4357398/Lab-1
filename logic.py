import csv
import os
from typing import Dict


class VoteManager:
    def __init__(self, filename: str = "votes.csv"):
        self.filename = filename
        self._votes = {"Bianca": 0, "Edward": 0, "Felicia": 0}
        self._load_votes()

    def _load_votes(self) -> None:
        if os.path.exists(self.filename):
            try:
                with open(self.filename, mode="r", newline="") as file:
                    reader = csv.reader(file)
                    next(reader)  # skip header
                    for row in reader:
                        if row[0] in self._votes:
                            self._votes[row[0]] = int(row[1])
            except Exception as e:
                raise IOError(f"Failed to read vote data: {e}")

    def _save_votes(self) -> None:
        try:
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Candidate", "Votes"])
                for candidate, count in self._votes.items():
                    writer.writerow([candidate, count])
        except Exception as e:
            raise IOError(f"Failed to save vote data: {e}")

    def add_vote(self, candidate: str) -> None:
        if candidate not in self._votes:
            raise ValueError("Invalid candidate")
        self._votes[candidate] += 1
        self._save_votes()

    def get_results(self) -> Dict[str, int]:
        return self._votes.copy()
