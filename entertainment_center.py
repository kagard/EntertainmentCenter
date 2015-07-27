"""A module that shows Keith's favorite movies on a dynamic web page."""

#-----------------------------------------------------------------------
# Name:        entertainment_center.py
# Purpose:      Show posters and trailers for some of my favorite films.
#
# Author:      Keith Gardner
#
# Created:     2015-07-17
#-----------------------------------------------------------------------
#ToDo1 [x] Add release date, movie stars.
#ToDo1 [x] Show storyline, year, stars below title
#ToDo3 [x] Improve css formatting
#ToDo1 [x] Check code formtting with PEP-8 & Pylint
#ToDo2 [x] Comment code
#ToDo1 [x] Add docstrings
#ToDo1 [] Create readme.txt
#ToDo1 [] Add project to Git.

import fresh_tomatoes as ft
import media

# Even though some of the URL arguments below are longer than
# recommended, I've left them in tact because they are easier to
# read and copy.

# Instantiate movie objects with key information.
interstellar = media.Movie(
    "Interstellar", "2014",
    "Matthew McConaughey, Anne Hathaway",
    "Adventurers search for a new Earth",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E"
    )

big_hero = media.Movie(
    "Big Hero 6", "2014", "Voices: Scott Adsit, Ryan Potter",
    "A boy loses his brother, but gains a puffy robotic friend",
    "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
    "https://www.youtube.com/watch?v=8IdMPpKMdcc"
    )

capt_phillips = media.Movie(
    "Captain Phillips", "2013", "Tom Hanks, Barkhad Abdi",
    "A U.S. container ship is hijacked by Somali parates",
    "https://upload.wikimedia.org/wikipedia/en/a/a8/Captain_Phillips_Poster.jpg",
    "https://www.youtube.com/watch?v=pV-ptQX-75Y"
    )

gravity = media.Movie(
    "Gravity", "2013", "Sandra Bullock, George Clooney",
    "A routine space mission - until everything goes wrong",
    "https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg",
    "https://www.youtube.com/watch?v=_KJHRF6RlTQ"
    )

the_rock = media.Movie(
    "The Rock", "1996", "Sean Connery, Nicolas Cage",
    "A long-imprisoned English spy and an American scientist must break into Alcatraz",
    "https://upload.wikimedia.org/wikipedia/en/8/82/The_Rock_%28movie%29.jpg",
    "https://www.youtube.com/watch?v=ClOQJAB0uD0"
    )

winter_soldier = media.Movie(
    "Captain America: The Winter Soldier", "2014",
    "Chris Evans, Robert Redford",
    "America's supersoldier faces a new challenge from the old days",
    "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",
    "https://www.youtube.com/watch?v=tbayiPxkUMM"
    )

movies = [interstellar, big_hero, capt_phillips,
          gravity, the_rock, winter_soldier
          ]

ft.open_movies_page(movies)