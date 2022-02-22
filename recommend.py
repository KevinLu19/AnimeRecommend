from lib2to3.pgen2.pgen import generate_grammar
import requests
from mal import *
from mal import AnimeSearch
import time

# Jikan API Restrictions:
# - 60 requests per minute
# - 3 requests per second

BASE_MY_ANIME_LIST_URL = "https://api.jikan.moe/v4"

class AnimeRecommend:
    def __init__(self, **kwargs):
        # print (kwargs)
        self.anime_id = kwargs["user_anime_id"]
        self.anime_score_threshold = 8                  # Filters anime by their MAL score.
    
    # Heart and soul of the class. 
    # Takes in any parameter that is needed to make Anime search funciton possible according to the API documentation.
    def request_to_API(self, **kwargs):
        re = requests.get(BASE_MY_ANIME_LIST_URL + str(*kwargs.values()))
        # print (kwargs)

        return re.json()
    
    # Takes query string and passes through API to which this function will print out useful information. 
    def get_anime_query(self, genre_list):
        # Convert genre_list to a string in order to comma separate it if list is > 1.
        if len(genre_list) > 1:
            convert_to_str = list(map(str, genre_list))
            joinned_string = ",".join(convert_to_str)
            
            # genres=22&score=8&order_by=popularity
            query_string = f"/anime?genres={joinned_string}&min_score={self.anime_score_threshold}&order_by=asc"
 
        else: 
            # genres=22&score=8&order_by=popularity
            query_string = f"/anime?genres={genre_list[0]}&min_score={self.anime_score_threshold}&order_by=asc"
 
        
        result = self.request_to_API(api_query = query_string)

        for anime in result["data"]:
            print ("=============================")
            print ("Title: " , anime["title"])
            print ("Score: ", anime["score"])
            print ("Type: ", anime["type"])         
            print ("Theme: ", [theme["name"] for theme in anime["themes"]])               # Returns back a list. Can return back nothing.
            print ("Demographic: ", [demog["name"] for demog in anime["demographics"]])   # Returns back a list. Can return back nothing.
            print ("Episodes: ", anime["episodes"])
            print ("MAL URL: ", anime["url"])
            print ("\n")
            print ("Synopsis: ", anime["synopsis"])
            print ("=============================")
            time.sleep(5)
            # print (anime)

    # This function is search a specific anime and return the genre, used for when user wants to recommend the anime they entered.
    def serach_user_entered_anime(self):
        # URL Layout for genre: https://api.jikan.moe/v4/anime/48736
        full_query_command = f"/anime/{self.anime_id}"
        results = self.request_to_API(api_query=full_query_command)

        # print (full_query_command)
        # print(results)

        anime_genre_list = []

        for genre in results["data"]["genres"]:
            anime_genre_list.append(genre["mal_id"])
           # anime_genre_list.append(genre["name"])

        print("Genre: ", anime_genre_list)

        for theme in results["data"]["themes"]:
            print ("Theme: ", theme["name"])

        for demographic in results["data"]["demographics"]:
            print ("Demographic: ", demographic["name"])

        self.get_anime_query(anime_genre_list)

    # /anime?genres=22&score=8&order_by=popularity

def main():
#     GENRE = "genre"
#     choice_prompt = input("Enter in genre to recommend anime genre or name to recommend anime by name: ")

#     # user_requested_anime = "Sono Bisque doll wa koi wo suru"
#     genre_numeric_id = """
# 1 - Action       | 2 - Adventure 
# 4 - Comedy       | 7 - Mystery 
# 8 - Drama        | 9 - Ecchi 
# 10 - Fantasy     | 14 - Horror 
# 22 - Romance     | 24 - Sci-Fi 
# 30 - Sport       | 36 - Slice - of - Life 
# 37 - Supernatural| 41 - Suspense 
# 47 - Gourmet 

#    **Note: If you want to add more than one genre, separate them using a comma(,)
# """
    ## Can't search by Genre since it requires anime_id in order to do so.
    # if choice_prompt.upper() == GENRE.upper():
    #     # user types in genre
    #     print (genre_numeric_id)

    #     user_requested_genre_id = input("Enter your genre using , as delimiter for multiple: ")
    #     new_requested_genre_id = user_requested_genre_id.replace(" ", "")

    #     # Value for user_anime_id here doesn't exist since its searching via genre. Put in an invalid id to avoid the error.
    #     anime_reco = AnimeRecommend(user_genre = new_requested_genre_id, user_anime_id = 0)
    #     anime_reco.serach_user_entered_anime()

    # else:
    #     user_requested_anime = input("Enter Anime: ")

    #     anime_id = AnimeSearch(user_requested_anime).results[0].mal_id
    #     # Value for user_genre here does not exist. Was throwing an error saying kwargs["user_genre"] didn't exist which is true.
    #     anime_reco = AnimeRecommend(user_anime_id = anime_id, user_genre = 11)
    #     anime_reco.serach_user_entered_anime()
        
    # user_requested_anime = input("Enter Anime: ")
    
    user_requested_anime = input("Enter Anime: ")
    anime_id = AnimeSearch(user_requested_anime).results[0].mal_id
    # Value for user_genre here does not exist. Was throwing an error saying kwargs["user_genre"] didn't exist which is true.
    anime_reco = AnimeRecommend(user_anime_id = anime_id, user_genre = 11)
    anime_reco.serach_user_entered_anime()

    # Testing purposes.
    # user_given_genre = 22


    # anime_reco.get_anime_query()
    # anime_reco.serach_user_entered_anime()
    
main()