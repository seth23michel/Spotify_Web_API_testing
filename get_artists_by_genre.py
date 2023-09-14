import requests
import json
from get_token import get_access_token  # Assuming you have this function in a file called get_token.py

def get_artists_by_genre(token, genre):
    search_url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": f"genre:{genre}",
        "type": "artist",
        "limit": 10  # You can change this to fetch more or fewer artists
    }

    r = requests.get(search_url, headers=headers, params=params)
    result = r.json()

    # Extracting the artist info
    artist_list = []
    for artist in result['artists']['items']:
        artist_data = {
            "name": artist["name"],
            "id": artist["id"],
            "popularity": artist["popularity"],
            "genres": artist["genres"],
            "external_urls": artist["external_urls"]["spotify"],
            "followers": artist["followers"]["total"],
            "images": artist["images"][0]["url"] if artist["images"] else None  # Grabbing the first image if available
        }
        artist_list.append(artist_data)

    return artist_list


if __name__ == "__main__":
    token = get_access_token()  # Retrieve the token
    genre = input("Enter Genre: ")  # Replace this with the genre you're interested in
    artists = get_artists_by_genre(token, genre)

    # Print the list of artists in a readable format
    for artist in artists:
        print(f"Artist: {artist['name']}")
        print(f"ID: {artist['id']}")
        print(f"Popularity: {artist['popularity']}")
        print(f"Genres: {', '.join(artist['genres'])}")
        print(f"Spotify URL: {artist['external_urls']}")
        print(f"Followers: {format(artist['followers'], ',')}")
        print(f"Image: {artist['images']}")
        print("----------")

