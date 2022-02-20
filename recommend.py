import requests

# Jikan API Restrictions:
# - 60 requests per minute
# - 3 requests per second

BASE_MY_ANIME_LIST_URL = "https://api.jikan.moe/v4"

def get_anime_genre(anime_id):
    re = requests.get(BASE_MY_ANIME_LIST_URL + str(f"/anime/{anime_id}"))   
    results = re.json()

    anime_genre_list = []

    for genre in  results["data"]["genres"]:
        anime_genre_list.append(genre["name"])

    print (anime_genre_list)       


def main():
    # user_requested_anime = input("Enter Anime: ")
    
    # if " " in user_requested_anime:
    #     new_user_requested_anime = user_requested_anime.replace(" ", "_")
    #     print (new_user_requested_anime)
    # else:
    #     print(user_requested_anime)

    get_anime_genre(48736)

main()