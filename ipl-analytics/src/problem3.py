"""Problem 3: Foreign umpire analysis."""

import csv
import matplotlib.pyplot as plt
from constants import MATCHES_FILE, UMPIRE1, UMPIRE2

# Umpire country mapping (sourced from research)
UMPIRE_COUNTRIES = {
    'Aleem Dar': 'Pakistan',
    'Kumar Dharmasena': 'Sri Lanka',
    'Simon Taufel': 'Australia',
    'Ian Gould': 'England',
    'Billy Bowden': 'New Zealand',
    'Marais Erasmus': 'South Africa',
    'Paul Reiffel': 'Australia',
    'Rod Tucker': 'Australia',
    'Richard Kettleborough': 'England',
    'Chris Gaffaney': 'New Zealand',
    'Bruce Oxenford': 'Australia',
    'Nigel Llong': 'England',
    'Michael Gough': 'England',
    'Joel Wilson': 'West Indies',
    'Richard Illingworth': 'England',
    'Chris Brown': 'New Zealand',
    'SJ Davis': 'Australia',
    'RJ Tucker': 'Australia',
    'S Ravi': 'India',
    'C Shamshuddin': 'India',
    'Sundaram Ravi': 'India',
}


def calculate_foreign_umpires():
    """Count foreign umpires by country.

    Returns:
        dict: Country name as key, count of umpires as value
    """
    umpire_set = set()

    with open(MATCHES_FILE, 'r', encoding='utf-8') as file:
        matches_reader = csv.DictReader(file)

        for match in matches_reader:
            umpire1 = match[UMPIRE1]
            umpire2 = match[UMPIRE2]

            if umpire1 and umpire1 in UMPIRE_COUNTRIES:
                umpire_set.add(umpire1)
            if umpire2 and umpire2 in UMPIRE_COUNTRIES:
                umpire_set.add(umpire2)

    country_count = {}
    for umpire in umpire_set:
        country = UMPIRE_COUNTRIES[umpire]
        if country != 'India':
            if country in country_count:
                country_count[country] += 1
            else:
                country_count[country] = 1

    return country_count


def plot_foreign_umpires(country_count):
    """Plot foreign umpires by country.

    Args:
        country_count (dict): Country name as key, count as value
    """
    countries = list(country_count.keys())
    counts = list(country_count.values())

    plt.figure(figsize=(10, 6))
    plt.bar(countries, counts, color='teal', edgecolor='darkslategray')
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Number of Umpires', fontsize=12)
    plt.title('Foreign Umpires in IPL by Country', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('problem3_foreign_umpires.png', dpi=300)
    print("Chart saved: problem3_foreign_umpires.png")
    plt.close()


def execute():
    """Execute problem 3 analysis."""
    print("Problem 3: Analyzing foreign umpires...")
    country_count = calculate_foreign_umpires()
    plot_foreign_umpires(country_count)
    print("Problem 3: Complete!\n")


if __name__ == '__main__':
    execute()
