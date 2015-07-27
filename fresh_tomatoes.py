import webbrowser
import os
import re

# Moved css and html elements to separate files for clarity and ease
# of editing. This results in a small performance hit, but worth it
# for a small page like this.

# Styles and scripting for the page
the_header = open("fresh_header.htm")
main_page_head = the_header.read()
the_header.close()

# The main page layout and title bar
page_content = open("fresh_body.htm")
main_page_content = page_content.read()
page_content.close()

# A single movie entry html template
the_title = open("fresh_movie.htm")
movie_tile_content = the_title.read()
the_title.close()

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        stars = movie.stars
        stars = stars.replace(", ", "<br />")
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_release_date=movie.released,
            movie_stars=stars,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible