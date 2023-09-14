import requests
from get_token import get_access_token  # Assuming you have this function in a file called get_token.py

def get_artist_id(token, artist_name):
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
    return result['artists']['items'][0]['id']


def get_albums(token, artist_id):
    albums_url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    r = requests.get(albums_url, headers=headers)
    result = r.json()
    albums = [album['name'] for album in result['items']]
    return albums


if __name__ == "__main__":
    token = get_access_token()  # Retrieve token
    artist_name = "Kanye West"
    artist_id = get_artist_id(token, artist_name)
    albums = get_albums(token, artist_id)
    print(albums)
