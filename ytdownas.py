from youtube_search import YoutubeSearch
import os

# filenames = next(walk("/media/hex24/3863-5EE5"), (None, None, []))[2]  # [] if no file
def downloadVideo(filename):
    result = YoutubeSearch(os.path.basename(filename), max_results=1).to_dict()[0]
    title = result['title']
    url = result['url_suffix']

    os.system(f"yt-dlp -x --audio-format mp3 --audio-quality 0 'https://www.youtube.com{url}' -o '{title}'")

    return './'+ title + '.mp3'