class VoteTracker:
    """Class for managing vote tallies."""

    def __init__(self) -> None:
        """Initialize the vote tracker with candidates."""
        self.votes = {"Bianca": 0, "Edward": 0, "Felicia": 0}

    def vote(self, candidate: str) -> bool:
        """
        Increment vote for a valid candidate.

        Args:
            candidate (str): The candidate to vote for.

        Returns:
            bool: True if vote is cast successfully, False otherwise.
        """
        if candidate in self.votes:
            self.votes[candidate] += 1
            return True
        return False

    def get_results(self) -> dict[str, int]:
        """
        Return current vote results.

        Returns:
            dict[str, int]: Dictionary of candidate names and vote counts.
        """
        return self.votes

    def reset(self) -> None:
        """
        Reset all vote counts to zero.
        """
        for candidate in self.votes:
            self.votes[candidate] = 0
