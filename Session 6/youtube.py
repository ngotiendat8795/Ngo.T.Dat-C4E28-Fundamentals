from youtube_dl import YoutubeDL

option = {
    'default_search':'ytsearch',
    'max_downloads': 1,
    'format':'bestaudio/audio'
}

dl = YoutubeDL(option)
dl.download(['too good at good bye'])




