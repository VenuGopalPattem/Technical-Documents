"""IPL Data Analytics - Main execution file."""

import problem1
import problem2
import problem3
import problem4
import problem5
import problem6
import problem7
import problem8


def execute():
    """Execute all IPL analysis problems."""
    print("=" * 60)
    print("IPL DATA ANALYTICS")
    print("=" * 60)
    print()

    problem1.execute()
    problem2.execute()
    problem3.execute()
    problem4.execute()
    problem5.execute()
    problem6.execute()
    problem7.execute()
    problem8.execute()

    print("=" * 60)
    print("ALL ANALYSIS COMPLETE!")
    print("=" * 60)


if __name__ == '__main__':
    execute()
