from bs4 import BeautifulSoup
import requests


def get_billboard_url():
    year_str = input('What year do you want to time travel to?  Type the date in this format YYYY-MM-DD: ')
    return f"https://www.billboard.com/charts/hot-100/{year_str}/"


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
    song_list, artist_list = get_song_list(get_billboard_url())

    print(artist_list)
    print(song_list)
