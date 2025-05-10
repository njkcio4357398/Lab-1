import csv
import os

def save_votes_to_csv(votes: dict[str, int], filename: str = "data/votes.csv") -> None:
    """Save votes to a CSV file."""
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Candidate", "Votes"])
            for candidate, count in votes.items():
                writer.writerow([candidate, count])
    except Exception as e:
        print(f"Error saving votes: {e}")


def load_votes_from_csv(filename: str = "data/votes.csv") -> dict[str, int]:
    """
    Load votes from a CSV file into a dictionary.

    Returns:
        dict[str, int]: Dictionary of candidate names and their vote counts.
    """
    votes: dict[str, int] = {"Bianca": 0, "Edward": 0, "Felicia": 0}  # default structure

    if not os.path.exists(filename):
        return votes  # Return defaults if file doesn't exist

    try:
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get("Candidate")
                count = row.get("Votes")
                if name in votes and count is not None and count.isdigit():
                    votes[name] = int(count)
    except Exception as e:
        print(f"Error loading votes: {e}")

    return votes
