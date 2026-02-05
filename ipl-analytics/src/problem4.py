"""Problem 4: Stacked chart of matches played by team by season."""

import csv
import matplotlib.pyplot as plt
from constants import MATCHES_FILE, SEASON, TEAM1, TEAM2


def calculate_matches_by_team_season():
    """Calculate number of matches played by each team per season.

    Returns:
        tuple: (seasons list, teams list, matches_data dict)
    """
    matches_data = {}

    with open(MATCHES_FILE, 'r', encoding='utf-8') as file:
        matches_reader = csv.DictReader(file)

        for match in matches_reader:
            season = match[SEASON]
            team1 = match[TEAM1]
            team2 = match[TEAM2]

            if season not in matches_data:
                matches_data[season] = {}

            if team1 in matches_data[season]:
                matches_data[season][team1] += 1
            else:
                matches_data[season][team1] = 1

            if team2 in matches_data[season]:
                matches_data[season][team2] += 1
            else:
                matches_data[season][team2] = 1

    all_teams = set()
    for season_teams in matches_data.values():
        all_teams.update(season_teams.keys())

    seasons = sorted(matches_data.keys())
    teams = sorted(all_teams)

    return seasons, teams, matches_data


def plot_stacked_matches(seasons, teams, matches_data):
    """Plot stacked bar chart of matches by team by season.

    Args:
        seasons (list): List of seasons
        teams (list): List of all teams
        matches_data (dict): Nested dict with season->team->count
    """
    team_season_data = {team: [] for team in teams}

    for season in seasons:
        for team in teams:
            count = matches_data[season].get(team, 0)
            team_season_data[team].append(count)

    plt.figure(figsize=(14, 8))
    bottom = [0] * len(seasons)

    for team in teams:
        plt.bar(seasons, team_season_data[team], bottom=bottom, label=team, edgecolor='white')
        bottom = [bottom[i] + team_season_data[team][i] for i in range(len(seasons))]

    plt.xlabel('Season', fontsize=12)
    plt.ylabel('Number of Matches', fontsize=12)
    plt.title('Matches Played by Team by Season', fontsize=14, fontweight='bold')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('problem4_matches_by_team_season.png', dpi=300)
    print("Chart saved: problem4_matches_by_team_season.png")
    plt.close()


def execute():
    """Execute problem 4 analysis."""
    print("Problem 4: Analyzing matches by team by season...")
    seasons, teams, matches_data = calculate_matches_by_team_season()
    plot_stacked_matches(seasons, teams, matches_data)
    print("Problem 4: Complete!\n")


if __name__ == '__main__':
    execute()
