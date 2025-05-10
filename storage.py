import csv

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
