
import requests

base_url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

def list_artists () -> list:
    """
    List all available artists from an API.

    Returns:
        list: A A list containing the names of every available artist.
    """
    data = requests.get(base_url)
    data = data.json()
    artists = data["artists"]

    artist_list = []

    for artist in artists:
           artist_list.append(artist["name"])

    return artist_list

def get_artist_by_id(artist_id: str) -> dict:
    """
    Get information about a specific artist from an API.

    Args:
        get_artist_by_id (str): A string representing the id of the artist to search for.

    Returns:
        dict: A dictionary containing information about the artist, including their name, ID, and other details.
    """
    url = f"{base_url}{artist_id}"

    artist_info = requests.get(url)
    artist_info = artist_info.json()
    artist_info = artist_info["artist"]

    return artist_info

def get_artist(artist_name: str) -> dict:
    """
    Get information for a specific artist from an API.

    Args:
        artist_name: A string representing the name of the artist to retrieve.

    Returns:
        A dictionary containing information about the artist, including their name, ID, and other details.
    """
    data = requests.get(base_url)
    data = data.json()
    artists = data["artists"]

    artist_id = None

    for artist in artists:
        if artist["name"] == artist_name:
            artist_id = artist["id"]
            
    url = f"{base_url}{artist_id}"
    artist_info = requests.get(url)
    artist_info = artist_info.json()
    artist_info = artist_info["artist"]

    return artist_info