"""Problem 6: Number of matches won per team per year."""

import csv
import matplotlib.pyplot as plt
from constants import MATCHES_FILE, SEASON, WINNER


def calculate_wins_by_team_year():
    """Calculate wins by team per year.

    Returns:
        tuple: (years list, teams list, wins_data dict)
    """
    wins_data = {}

    with open(MATCHES_FILE, 'r', encoding='utf-8') as file:
        matches_reader = csv.DictReader(file)

        for match in matches_reader:
            year = match[SEASON]
            winner = match[WINNER]

            if not winner:
                continue

            if year not in wins_data:
                wins_data[year] = {}

            if winner in wins_data[year]:
                wins_data[year][winner] += 1
            else:
                wins_data[year][winner] = 1

    all_teams = set()
    for year_teams in wins_data.values():
        all_teams.update(year_teams.keys())

    years = sorted(wins_data.keys())
    teams = sorted(all_teams)

    return years, teams, wins_data


def plot_stacked_wins(years, teams, wins_data):
    """Plot stacked bar chart of wins by team by year.

    Args:
        years (list): List of years
        teams (list): List of all teams
        wins_data (dict): Nested dict with year->team->wins
    """
    team_year_data = {team: [] for team in teams}

    for year in years:
        for team in teams:
            wins = wins_data[year].get(team, 0)
            team_year_data[team].append(wins)

    plt.figure(figsize=(14, 8))
    bottom = [0] * len(years)

    for team in teams:
        plt.bar(years, team_year_data[team], bottom=bottom, label=team, edgecolor='white')
        bottom = [bottom[i] + team_year_data[team][i] for i in range(len(years))]

    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Wins', fontsize=12)
    plt.title('Matches Won per Team per Year in IPL', fontsize=14, fontweight='bold')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('problem6_wins_by_team_year.png', dpi=300)
    print("Chart saved: problem6_wins_by_team_year.png")
    plt.close()


def execute():
    """Execute problem 6 analysis."""
    print("Problem 6: Analyzing wins by team by year...")
    years, teams, wins_data = calculate_wins_by_team_year()
    plot_stacked_wins(years, teams, wins_data)
    print("Problem 6: Complete!\n")


if __name__ == '__main__':
    execute()
