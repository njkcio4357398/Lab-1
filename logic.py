class VoteTracker:
    """Class for managing vote tallies."""

    def __init__(self) -> None:
        self.votes = {"Bianca": 0, "Edward": 0, "Felicia": 0}

    def vote(self, candidate: str) -> bool:
        """Increment vote for a valid candidate."""
        if candidate in self.votes:
            self.votes[candidate] += 1
            return True
        return False

    def get_results(self) -> dict[str, int]:
        """Return current vote results."""
        return self.votes
