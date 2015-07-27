#-----------------------------------------------------------------------
# Name:        media.py
# Purpose:     Movie info class
#
# Author:      Keith Gardner
#
# Created:     2015-07-17
# Copyright:   (c) Keith Gardner
#-----------------------------------------------------------------------
#ToDo1 [x] Add docstring
#ToDo1 [x] Add stars, release date

import webbrowser


class Movie():
    """
    Stores basic information about a movie.

    Attributes:
        - title: full title of the movie.
        - released: year the movie was released
        - stars: a list of the movie's start.
        - storyline: brief description of the plot
        - poster_url: link to poster image.
        - trailer_url: link to trailer on YouTube

    Methods:
        - show_trailer() - Plays the movie's trailer
    """

    def __init__(self, movie_title, release_year, movie_stars,
                 movie_storyline, poster_image, trailer_youtube):
        """
        Initialize move object

        Provide title, release year, stars, storyline,
        poster url and trailer url.
        """
        self.title = movie_title
        self.released = release_year
        self.stars = movie_stars
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Show the movie trailer."""
        webbrowser.open(self.trailer_youtube_url)