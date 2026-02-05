"""Problem 8: Top 10 economical bowlers in 2015."""

import csv
import matplotlib.pyplot as plt
from constants import (DELIVERIES_FILE, MATCHES_FILE, MATCH_ID,
                       MATCH_ID_COL, SEASON, BOWLER, TOTAL_RUNS)


def get_2015_match_ids():
    """Get all match IDs from 2015 season.

    Returns:
        set: Set of match IDs from 2015
    """
    match_ids_2015 = set()

    with open(MATCHES_FILE, 'r', encoding='utf-8') as file:
        matches_reader = csv.DictReader(file)

        for match in matches_reader:
            if match[SEASON] == '2015':
                match_ids_2015.add(match[MATCH_ID_COL])

    return match_ids_2015


def calculate_bowler_economy_2015():
    """Calculate economy rate for bowlers in 2015.

    Returns:
        dict: Bowler name as key, economy rate as value
    """
    match_ids_2015 = get_2015_match_ids()
    bowler_stats = {}

    with open(DELIVERIES_FILE, 'r', encoding='utf-8') as file:
        deliveries_reader = csv.DictReader(file)

        for delivery in deliveries_reader:
            match_id = delivery[MATCH_ID]

            if match_id in match_ids_2015:
                bowler = delivery[BOWLER]
                runs = int(delivery[TOTAL_RUNS])

                if bowler not in bowler_stats:
                    bowler_stats[bowler] = {'runs': 0, 'balls': 0}

                bowler_stats[bowler]['runs'] += runs
                bowler_stats[bowler]['balls'] += 1

    bowler_economy = {}
    for bowler, stats in bowler_stats.items():
        if stats['balls'] >= 24:
            overs = stats['balls'] / 6
            economy = stats['runs'] / overs
            bowler_economy[bowler] = economy

    return bowler_economy


def plot_top_economical_bowlers(bowler_economy):
    """Plot top 10 economical bowlers in 2015.

    Args:
        bowler_economy (dict): Bowler name as key, economy rate as value
    """
    sorted_bowlers = sorted(bowler_economy.items(), key=lambda x: x[1])
    top_10 = sorted_bowlers[:10]

    bowlers = [item[0] for item in top_10]
    economies = [item[1] for item in top_10]

    plt.figure(figsize=(12, 6))
    plt.barh(bowlers, economies, color='green', edgecolor='darkgreen')
    plt.xlabel('Economy Rate', fontsize=12)
    plt.ylabel('Bowler', fontsize=12)
    plt.title('Top 10 Economical Bowlers in 2015', fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('problem8_economical_bowlers_2015.png', dpi=300)
    print("Chart saved: problem8_economical_bowlers_2015.png")
    plt.close()


def execute():
    """Execute problem 8 analysis."""
    print("Problem 8: Calculating economical bowlers in 2015...")
    bowler_economy = calculate_bowler_economy_2015()
    plot_top_economical_bowlers(bowler_economy)
    print("Problem 8: Complete!\n")


if __name__ == '__main__':
    execute()
