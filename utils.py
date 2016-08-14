""" A utility module """

import json
import media
import requests

def get_movie_object_list(movies):
    """
        Given a list of movie names, return a list of object
        for each movie present in the movie list
    """

    # List of Movie objects to be returned
    data = []
    for movie in movies:
        
        # Get the info of movie from the OMDB API (http://www.omdbapi.com/)
        request = requests.get("http://www.omdbapi.com/?t=" + movie)
        # request.content returns bytes, convert it to str using decode()
        movie_info = json.loads(request.content.decode("utf-8"))

        # Create Movie object with title and storyline
        movie_object = media.Movie(movie_title=movie,
                                   movie_storyline=movie_info["Plot"])
        data.append(movie_object)

    return data
