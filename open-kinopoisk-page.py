#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, exit, stderr
from webbrowser import open_new_tab
from guessit import guessit


def get_kinopoisk_url(filename):
    result = None
    g = guessit(filename)
    t = g["title"]
    if "year" in g:
        t = "{} {}".format(t, g["year"])
    result = t.replace(' ', '+')
    search_query = "https://www.kinopoisk.ru/index.php?kp_query="
    search_query += result
    return search_query


if __name__ == "__main__":
    try:
        url = get_kinopoisk_url(argv[1])
        open_new_tab(url)
    except ValueError:
        stderr.write("Failed to find kinopoisk URL")
        exit(1)
