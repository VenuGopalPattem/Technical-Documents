"""Problem 1: Total runs scored by each team over IPL history."""

import csv
import matplotlib.pyplot as plt
from constants import DELIVERIES_FILE, BATTING_TEAM, TOTAL_RUNS


def calculate_total_runs_by_team():
    """Calculate total runs scored by each team.
    
    Returns:
        dict: Team name as key, total runs as value
    """
    team_runs = {}
    with open(DELIVERIES_FILE, 'r', encoding='utf-8') as file:
        deliveries_reader = csv.DictReader(file)
        for delivery in deliveries_reader:
            team = delivery[BATTING_TEAM]
            runs = int(delivery[TOTAL_RUNS])
            if team in team_runs:
                team_runs[team] += runs
            else:
                team_runs[team] = runs
    return team_runs
def plot_total_runs_by_team(team_runs):
    """Plot bar chart of total runs by team.
    
    Args:
        team_runs (dict): Team name as key, total runs as value
    """
    teams = list(team_runs.keys())
    runs = list(team_runs.values())
    plt.figure(figsize=(12, 6))
    plt.bar(teams, runs, color='skyblue', edgecolor='navy')
    plt.xlabel('Team', fontsize=12)
    plt.ylabel('Total Runs', fontsize=12)
    plt.title('Total Runs Scored by Each Team in IPL History', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('problem1_total_runs_by_team.png', dpi=300)
    print("Chart saved: problem1_total_runs_by_team.png")
    plt.close()


def execute():
    """Execute problem 1 analysis."""
    print("Problem 1: Calculating total runs by team...")
    team_runs = calculate_total_runs_by_team()
    plot_total_runs_by_team(team_runs)
    print("Problem 1: Complete!\n")


if __name__ == '__main__':
    execute()
