"""Problem 5: Number of matches played per year."""

import csv
import matplotlib.pyplot as plt
from constants import MATCHES_FILE, SEASON


def calculate_matches_per_year():
    """Calculate number of matches played per year.

    Returns:
        dict: Year as key, number of matches as value
    """
    year_matches = {}

    with open(MATCHES_FILE, 'r', encoding='utf-8') as file:
        matches_reader = csv.DictReader(file)

        for match in matches_reader:
            year = match[SEASON]

            if year in year_matches:
                year_matches[year] += 1
            else:
                year_matches[year] = 1

    return year_matches


def plot_matches_per_year(year_matches):
    """Plot bar chart of matches per year.

    Args:
        year_matches (dict): Year as key, count as value
    """
    years = sorted(year_matches.keys())
    matches = [year_matches[year] for year in years]

    plt.figure(figsize=(12, 6))
    plt.bar(years, matches, color='orange', edgecolor='darkorange')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Matches', fontsize=12)
    plt.title('Number of Matches Played per Year in IPL', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('problem5_matches_per_year.png', dpi=300)
    print("Chart saved: problem5_matches_per_year.png")
    plt.close()


def execute():
    """Execute problem 5 analysis."""
    print("Problem 5: Calculating matches per year...")
    year_matches = calculate_matches_per_year()
    plot_matches_per_year(year_matches)
    print("Problem 5: Complete!\n")


if __name__ == '__main__':
    execute()
