import requests
from mal import *
from mal import AnimeSearch

# Jikan API Restrictions:
# - 60 requests per minute
# - 3 requests per second

BASE_MY_ANIME_LIST_URL = "https://api.jikan.moe/v4"

def get_anime_query(**kwargs):
    # How to use Kwargs: 
    # Ex: get_anime_query(score = 9)
    score = kwargs.get("score", None)
    genre = kwargs.get("genre", None)
    order_by = kwargs.get("order_by", None)

def get_anime_genre(anime_id):
    re = requests.get(BASE_MY_ANIME_LIST_URL + str(f"/anime/{anime_id}"))   
    results = re.json()

    # print (results["data"]["genres"])

    anime_genre_list = []

    for genre in  results["data"]["genres"]:
        anime_genre_list.append(genre["name"])


    print (anime_genre_list)

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

    get_anime_genre(anime_id)

    # 48736 = Sono Bisque doll wa koi wo suru
    # get_anime_genre(48736)
    
main()