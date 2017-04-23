import media
import fresh_tomatoes

ToyStory = media.Movie("Toy Story",
                            "http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg",
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

Apollo13 = media.Movie("Apollo 13",
                            "http://img.moviepostershop.com/apollo-13-movie-poster-1995-1020190947.jpg",
                            "https://www.youtube.com/watch?v=nEl0NsYn1fU")

SleeplessInSeattle = media.Movie("Sleepless In Seattle",
                            "http://www.gstatic.com/tv/thumb/movieposters/14843/p14843_p_v8_aa.jpg",
                            "https://www.youtube.com/watch?v=-Lj2U-cmyek")

AHologramForTheKing = media.Movie("A Hologram For The King",
                                  "https://i.jeded.com/i/a-hologram-for-the-king-2016.51316.jpg",
                                  "https://www.youtube.com/watch?v=UW4OE1egbHs")
                                  


movie_list =  [ToyStory,Apollo13, SleeplessInSeattle,AHologramForTheKing]
fresh_tomatoes.open_movies_page(movie_list)
