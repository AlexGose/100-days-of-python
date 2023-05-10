from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_USER_NAME = os.getenv('SPOTIFY_USER_NAME')

def get_billboard_url():
    date_str = input('What year do you want to time travel to?  Type the date in this format YYYY-MM-DD: ')
    return f"https://www.billboard.com/charts/hot-100/{date_str}", date_str[:4]


def get_song_list(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    artists = []
    songs = []
    for index in range(1, 101):
        row = soup.select(selector=f'ul[data-detail-target="{index}"]')
        songs.append(row[0].find("h3").getText().strip())
        artists.append(row[0].select("li ul li span")[0].getText().strip())
    return songs, artists


if __name__ == '__main__':
    billboard_url, billboard_year = get_billboard_url()
    song_list, artist_list = get_song_list(billboard_url)

    scope = "playlist-modify-private"

    spotify = SpotifyOAuth(scope=scope)

    # access_token = spotify.get_access_token()

    sp = spotipy.Spotify(oauth_manager=spotify)

    print('Creating playlist...')
    playlist = sp.user_playlist_create(name=f'Billboard Top100 {billboard_year}', user=SPOTIFY_USER_NAME, public=False)

    track_uris = []
    counter = 1
    print('Adding tacks to playlist...')
    for song, artist in zip(song_list, artist_list):
        search_result = sp.search(f"track: {song} artist: {artist} year: {billboard_year}", limit=1, market="US")
        track_uris.append(search_result['tracks']['items'][0]['uri'])
        print(f"{counter}:")
        print("artist:", search_result['tracks']['items'][0]['artists'][0]['name'])
        print("track:", search_result['tracks']['items'][0]['name'])
        print("release date:", search_result['tracks']['items'][0]['album']['release_date'])
        print("uri:", search_result['tracks']['items'][0]['uri'])
        print()
        counter += 1

    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)
