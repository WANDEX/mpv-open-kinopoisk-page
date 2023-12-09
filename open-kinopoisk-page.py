#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from sys import argv, exit
from webbrowser import open_new_tab

try:
    from guessit import guessit
except ImportError as err:
    print(f"{err.msg}\nERROR: 'guessit' must be installed in the system!\n")
    exit(42)


def get_kinopoisk_url(filename):
    g = guessit(filename)
    t = g["title"]
    if "year" in g:
        t = "{} {}".format(t, g["year"])
    result = t.replace(' ', '+')
    return f"https://www.kinopoisk.ru/index.php?kp_query={result}"


if __name__ == "__main__":
    try:
        url = get_kinopoisk_url(argv[1])
        print("Opening URL in browser")
        open_new_tab(url)
    except ValueError:
        print("Failed to find kinopoisk URL")
        exit(1)
