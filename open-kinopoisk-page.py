#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, exit, stderr
from webbrowser import open_new_tab

from guessit import guessit
from kinopoisk.movie import Movie


def get_kinopoisk_url(filename):
    result = None
    g = guessit(filename)
    t = g["title"]
    if "year" in g:
        t = "{} {}".format(t, g["year"])
    results = Movie.objects.search(t)
    fid = results[0].id
    result = Movie(id=fid)
    url = "/film/{0}/".format(str(result.id))
    result.set_url(result.title_en, url)
    return result.get_url(result.title_en)


if __name__ == "__main__":
    try:
        url = get_kinopoisk_url(argv[1])
        open_new_tab(url)
    except ValueError:
        stderr.write("Failed to find kinopoisk URL")
        exit(1)
