# This file defines the Movie class

import webbrowser


class Movie():
    # The Movie class contains all the required information
    # for the movies to display on the final web page

    def __init__(self, movie_title, movie_storyline, movie_poster,
                 movie_trailer, movie_director, movie_release_date):
        # Initialize the movie with the required information

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        self.director = movie_director
        self.release_date = movie_release_date

    def play_trailer(self):
        # Play the trailer for the movie in the browser

        webbrowser.open(self.trailer)
