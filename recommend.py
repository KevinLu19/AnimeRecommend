from lib2to3.pgen2.pgen import generate_grammar
import requests
from mal import *
from mal import AnimeSearch

# Jikan API Restrictions:
# - 60 requests per minute
# - 3 requests per second

BASE_MY_ANIME_LIST_URL = "https://api.jikan.moe/v4"

class AnimeRecommend:
    def __init__(self, user_anime_id, user_genre):
        self.anime_id = user_anime_id
        self.anime_genre = user_genre
        self.anime_score_threshold = 8      # Filters anime by their MAL score.
 
    def request_to_API(self, **kwargs):
        re = requests.get(BASE_MY_ANIME_LIST_URL + str(*kwargs.values()))
        # print (kwargs)

        return re.json()

    def get_anime_query(self):
        # genres=22&score=8&order_by=popularity
        query_string = f"/anime?genres={self.anime_genre}&min_score={self.anime_score_threshold}&order_by=asc"
 
        result = self.request_to_API(api_query = query_string)

        for item in result["data"]:
            print (item["title"])


    def get_anime_genre(self):
        # URL Layout for genre: https://api.jikan.moe/v4/anime/48736
        full_query_command = f"/anime/{self.anime_id}"
        results = self.request_to_API(api_query=full_query_command)

        # print (results["data"]["genres"])

        anime_genre_list = []

        for genre in results["data"]["genres"]:
            anime_genre_list.append(genre["name"])

        print(anime_genre_list)


def main():
    # user_requested_anime = input("Enter Anime: ")
    user_requested_anime = "Sono Bisque doll wa koi wo suru"
    genre_numeric_id = """
1 - Action       | 2 - Adventure 
4 - Comedy       | 7 - Mystery 
8 - Drama        | 9 - Ecchi 
10 - Fantasy     | 14 - Horror 
22 - Romance     | 24 - Sci-Fi 
30 - Sport       | 36 - Slice - of - Life 
37 - Supernatural| 41 - Suspense 
47 - Gourmet 
"""
    print (genre_numeric_id)

    # user_given_genre = input("Enter your genre using , as delimiter for multiple: ")
    user_given_genre = 22

    anime_id = AnimeSearch(user_requested_anime).results[0].mal_id
    anime_reco = AnimeRecommend(anime_id, user_given_genre)

    # anime_reco.get_anime_genre()
    anime_reco.get_anime_query()
    
main()