"""Problem 2: Top 10 batsmen for Royal Challengers Bangalore."""

import csv
import matplotlib.pyplot as plt
from constants import DELIVERIES_FILE, BATTING_TEAM, BATSMAN, BATSMAN_RUNS


def calculate_rcb_batsman_runs():
    """Calculate runs scored by batsmen playing for RCB.

    Returns:
        dict: Batsman name as key, total runs as value
    """
    batsman_runs = {}

    with open(DELIVERIES_FILE, 'r', encoding='utf-8') as file:
        deliveries_reader = csv.DictReader(file)

        for delivery in deliveries_reader:
            team = delivery[BATTING_TEAM]

            if team == 'Royal Challengers Bangalore':
                batsman = delivery[BATSMAN]
                runs = int(delivery[BATSMAN_RUNS])

                if batsman in batsman_runs:
                    batsman_runs[batsman] += runs
                else:
                    batsman_runs[batsman] = runs

    return batsman_runs


def plot_top_rcb_batsmen(batsman_runs):
    """Plot top 10 RCB batsmen by runs.

    Args:
        batsman_runs (dict): Batsman name as key, total runs as value
    """
    sorted_batsmen = sorted(batsman_runs.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_batsmen[:10]

    batsmen = [item[0] for item in top_10]
    runs = [item[1] for item in top_10]

    plt.figure(figsize=(12, 6))
    plt.barh(batsmen, runs, color='crimson', edgecolor='darkred')
    plt.xlabel('Total Runs', fontsize=12)
    plt.ylabel('Batsman', fontsize=12)
    plt.title('Top 10 Batsmen for Royal Challengers Bangalore', fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('problem2_top_rcb_batsmen.png', dpi=300)
    print("Chart saved: problem2_top_rcb_batsmen.png")
    plt.close()


def execute():
    """Execute problem 2 analysis."""
    print("Problem 2: Calculating top RCB batsmen...")
    batsman_runs = calculate_rcb_batsman_runs()
    plot_top_rcb_batsmen(batsman_runs)
    print("Problem 2: Complete!\n")


if __name__ == '__main__':
    execute()
