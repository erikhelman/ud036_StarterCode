# This file defines the Movie class

import webbrowser

class Movie():

    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer, movie_director, movie_release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        self.director = movie_director
        self.release_date = movie_release_date

    #Open a browser and play the trailer
    def play_trailer(self):
        webbrowser.open(self.trailer)

