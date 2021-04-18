#!/usr/bin/env python3

from brain_games.implementer import welcome_user
from brain_games.games.gcd import gcd_numbers


def main():
    welcome_user()
    gcd_numbers()


if __name__ == '__main__':
    main()
