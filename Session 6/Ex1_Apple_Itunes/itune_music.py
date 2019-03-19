from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"

itunes = urlopen(url)

raw_code = itunes.read()
clean_code = raw_code.decode()

soup = BeautifulSoup(clean_code,"html.parser")
div = soup.find_all("div","section-content")

target=div[1]

li_list = target.find_all("li")

list_songs = []

for li in li_list:
    song_name = li.h3.string
    singer_name = li.h4.string
    matrix = OrderedDict({
        "Song name" : song_name,
        "Singer name": singer_name
    })
    list_songs.append(matrix)


for song in list_songs:

    option = {
        'default_search': 'ytsearch',
        'max_downloads':100,
        'format': 'bestaudio/audio'
    }

    dl = YoutubeDL(option)
    dl.download(song["Song name"]+song["Singer name"])

