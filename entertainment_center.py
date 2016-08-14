""" Module to build the application """

import fresh_tomatoes
import utils

movies = ["Toy Story", "Toy Story 2", "Toy Story 3", "Moneyball", "Wall street", "Suicide Squad"]

# Get list of Movie objects for the movies in movies list
list_of_movies_objects = utils.get_movie_object_list(movies)

# Add posters and yotube url's

# Toy story 1
list_of_movies_objects[0].poster_image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg"
list_of_movies_objects[0].trailer_youtube_url = "https://www.youtube.com/watch?v=KYz2wyBy3kc"

# Toy story 2
list_of_movies_objects[1].poster_image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/c/c0/Toy_Story_2.jpg/220px-Toy_Story_2.jpg"
list_of_movies_objects[1].trailer_youtube_url = "https://www.youtube.com/watch?v=Lu0sotERXhI" 

# Toy story 3
list_of_movies_objects[2].poster_image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/6/69/Toy_Story_3_poster.jpg/220px-Toy_Story_3_poster.jpg"
list_of_movies_objects[2].trailer_youtube_url = "https://www.youtube.com/watch?v=JcpWXaA2qeg"

# Moneyball
list_of_movies_objects[3].poster_image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/Moneyball_Poster.jpg/220px-Moneyball_Poster.jpg"
list_of_movies_objects[3].trailer_youtube_url = "https://www.youtube.com/watch?v=AiAHlZVgXjk"

# Wall street
list_of_movies_objects[4].poster_image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Wall_Street_film.jpg/220px-Wall_Street_film.jpg"
list_of_movies_objects[4].trailer_youtube_url = "https://www.youtube.com/watch?v=FCctqbRrsBQ"

# Suicide Squad
list_of_movies_objects[5].poster_image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/Suicide_Squad_%28film%29_Poster.png/220px-Suicide_Squad_%28film%29_Poster.png"
list_of_movies_objects[5].trailer_youtube_url = "https://www.youtube.com/watch?v=CmRih_VtVAs"

fresh_tomatoes.open_movies_page(list_of_movies_objects)
