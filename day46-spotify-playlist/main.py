from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':
    year_str = input('What year do you want to time travel to?  Type the date in this format YYYY-MM-DD: ')
    url = f"https://www.billboard.com/charts/hot-100/{year_str}/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    artists = []
    songs = []
    for index in range(1, 101):
        row = soup.select(selector=f'ul[data-detail-target="{index}"]')
        songs.append(row[0].find("h3").getText().strip())
        artists.append(row[0].select("li ul li span")[0].getText().strip())
    print(artists)
    print(songs)
