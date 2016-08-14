""" Movie Module """

import webbrowser

class Movie:
    """ Movie class """

    def __init__(self, movie_title, movie_storyline, poster_image = None, trailer_youtube = None):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Show trailer of a movie """
        webbrowser.open(self.tailer_youtube_url)
