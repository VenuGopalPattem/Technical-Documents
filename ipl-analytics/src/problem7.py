"""Problem 7: Extra runs conceded per team in 2016."""

import csv
import matplotlib.pyplot as plt
from constants import (DELIVERIES_FILE, MATCHES_FILE, MATCH_ID,
                       MATCH_ID_COL, SEASON, BOWLING_TEAM, EXTRA_RUNS)


def get_2016_match_ids():
    """Get all match IDs from 2016 season.

    Returns:
        set: Set of match IDs from 2016
    """
    match_ids_2016 = set()

    with open(MATCHES_FILE, 'r', encoding='utf-8') as file:
        matches_reader = csv.DictReader(file)

        for match in matches_reader:
            if match[SEASON] == '2016':
                match_ids_2016.add(match[MATCH_ID_COL])

    return match_ids_2016


def calculate_extra_runs_2016():
    """Calculate extra runs conceded by each team in 2016.

    Returns:
        dict: Team name as key, total extra runs as value
    """
    match_ids_2016 = get_2016_match_ids()
    team_extras = {}

    with open(DELIVERIES_FILE, 'r', encoding='utf-8') as file:
        deliveries_reader = csv.DictReader(file)

        for delivery in deliveries_reader:
            match_id = delivery[MATCH_ID]

            if match_id in match_ids_2016:
                team = delivery[BOWLING_TEAM]
                extras = int(delivery[EXTRA_RUNS])

                if team in team_extras:
                    team_extras[team] += extras
                else:
                    team_extras[team] = extras

    return team_extras


def plot_extra_runs_2016(team_extras):
    """Plot bar chart of extra runs by team in 2016.

    Args:
        team_extras (dict): Team name as key, extra runs as value
    """
    teams = list(team_extras.keys())
    extras = list(team_extras.values())

    plt.figure(figsize=(12, 6))
    plt.bar(teams, extras, color='purple', edgecolor='indigo')
    plt.xlabel('Team', fontsize=12)
    plt.ylabel('Extra Runs Conceded', fontsize=12)
    plt.title('Extra Runs Conceded per Team in 2016', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('problem7_extra_runs_2016.png', dpi=300)
    print("Chart saved: problem7_extra_runs_2016.png")
    plt.close()


def execute():
    """Execute problem 7 analysis."""
    print("Problem 7: Calculating extra runs in 2016...")
    team_extras = calculate_extra_runs_2016()
    plot_extra_runs_2016(team_extras)
    print("Problem 7: Complete!\n")


if __name__ == '__main__':
    execute()
