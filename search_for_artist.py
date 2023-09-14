import requests
import json
from get_token import get_access_token  # Assuming this function is in get_token.py

def get_artist_info(token, artist_name):
    search_url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": artist_name,
        "type": "artist",
        "limit": 1
    }
    r = requests.get(search_url, headers=headers, params=params)
    result = r.json()
    artist = result['artists']['items'][0]
    
    artist_data = {
        "name": artist["name"],
        "id": artist["id"],
        "popularity": artist["popularity"],
        "genres": ', '.join(artist["genres"]),
        "spotify_url": artist["external_urls"]["spotify"],
        "followers": artist["followers"]["total"],
        "image_url": artist["images"][0]["url"] if artist["images"] else "No image available"
    }
    return artist_data

if __name__ == "__main__":
    token = get_access_token()

    while True:
        print("1: Search for an artist")
        print("2: Quit")
        choice = input("Enter your choice (1/2): ")

        if choice == "2":
            print("Exiting program.")
            break
        elif choice == "1":
            search_query = input("\nEnter the name of the artist you're looking for: ")
            artist_info = get_artist_info(token, search_query)

            print(f"Artist: {artist_info['name']}")
            print(f"ID: {artist_info['id']}")
            print(f"Popularity: {artist_info['popularity']}")
            print(f"Genres: {artist_info['genres']}")
            print(f"Spotify URL: {artist_info['spotify_url']}")
            print(f"Followers: {format(artist_info['followers'], ',')}")
            print(f"Image URL: {artist_info['image_url']}")
            print("--------------------\n")
