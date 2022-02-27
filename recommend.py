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
        # /anime?genres=22&score=8&order_by=popularity
        full_query_command = f"/anime/{self.anime_id}"
        results = self.request_to_API(api_query=full_query_command)

        # print (full_query_command)
        # print(results)

        anime_genre_list = []
        anime_theme_list = []

        for genre in results["data"]["genres"]:
            anime_genre_list.append(genre["mal_id"])
           # anime_genre_list.append(genre["name"])

        print("Genre: ", anime_genre_list)

        for theme in results["data"]["themes"]:
            anime_theme_list.append(theme["name"])
            print ("Theme: ", theme["name"])
                
        for demographic in results["data"]["demographics"]:
            print ("Demographic: ", demographic["name"])

        
        self.get_anime_query(anime_genre_list)


def main():
    user_requested_anime = input("Enter Anime: ")
    anime_id = AnimeSearch(user_requested_anime).results[0].mal_id
    anime_reco = AnimeRecommend(user_anime_id = anime_id, user_genre = 11)
    anime_reco.serach_user_entered_anime()

main()