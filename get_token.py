import requests

def get_access_token():
    # Step 2: Setup your credentials
    client_id = 'e6e39cd9c5294f1fb7b131a372b0c1aa'
    client_secret = '3d5afa4d2c494df1a7b595c28e20b026'

    # Step 3: Construct headers and payload
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    # Step 4: Make the request
    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the access token from the JSON response
        access_token = response.json()['access_token']
        return access_token
    else:
        return None
