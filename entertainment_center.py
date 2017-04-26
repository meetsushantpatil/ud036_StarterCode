import fresh_tomatoes
import media

#Movie objects
#Add or remove Movie instances to add or remove your favourite movies. These are the ones for your reference.
#PS - Tom Hanks is my favourite.

toy_story = media.Movie(
            "Toy Story",
            "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

apollo13 = media.Movie(
	   "Apollo 13",
           "http://img.moviepostershop.com/apollo-13-movie-poster-1995-1020190947.jpg",
           "https://www.youtube.com/watch?v=nEl0NsYn1fU")

sleepless_in_seattle = media.Movie(
           "Sleepless In Seattle",
           "http://www.gstatic.com/tv/thumb/movieposters/14843/p14843_p_v8_aa.jpg",
           "https://www.youtube.com/watch?v=-Lj2U-cmyek")

a_hologram_for_the_king = media.Movie(
           "A Hologram For The King",
           "https://i.jeded.com/i/a-hologram-for-the-king-2016.51316.jpg",
           "https://www.youtube.com/watch?v=UW4OE1egbHs")

shawshank_redemption = media.Movie(
           "Shawshank Redemption",
           "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
           "https://www.youtube.com/watch?v=RLw6hBFJ8bk")

captain_philips = media.Movie(
	   "Captain Philips",
           "http://www.sonypictures.com/movies/captainphillips/assets/images/onesheet.jpg",
           "https://www.youtube.com/watch?v=a2AiLlYdJy8")

hobbit_an_unexpected_journey = media.Movie(
           "Hobbit - An Unexpected Journey",
           "http://t3.gstatic.com/images?q=tbn:ANd9GcTS1VqOgP7iJC44UcztFaTbvD0OzoRymEhXfMPlgq7FPY0OEvCj",
           "https://www.youtube.com/watch?v=y2M8BbTfZTA")

#Do not forget to add the instance name to this list.
movie_list =  [toy_story,
               apollo13,
               sleepless_in_seattle,
               a_hologram_for_the_king,
               shawshank_redemption,
               captain_philips,
               hobbit_an_unexpected_journey]

#Creating a static webpage & displaying the movie posters
fresh_tomatoes.open_movies_page(movie_list)
