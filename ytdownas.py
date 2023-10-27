from youtube_search import YoutubeSearch
import os
from hashlib import sha256
import yt_dlp

# Create a yt-dlp instance
ydl = yt_dlp.YoutubeDL()

# filenames = next(walk("/media/hex24/3863-5EE5"), (None, None, []))[2]  # [] if no file
def getVideoUrlTitle(query, seed):
    result = YoutubeSearch(query, max_results=seed).to_dict()[seed - 1]
    title = result['title']
    url = result['url_suffix']
    return (url, title)

def downloadVideo(url, title):

    hashedTitle = sha256(title.encode('utf-8')).hexdigest()

    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Set the preferred codec to mp3
            'preferredquality': '192'  # Set the preferred audio quality
        }],
        'outtmpl' : f'./music/{hashedTitle}'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.extract_info(f'https://www.youtube.com{url}', download=True)

    path = './music/'+ hashedTitle + '.mp3'

    return path

# downloadVideo("hello")