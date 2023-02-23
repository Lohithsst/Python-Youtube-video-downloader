from pytube import YouTube
from pytube import Playlist


def download(link, filepath):
    # Get video of highest quality
    vid = YouTube(link).streams.get_highest_resolution()

    if vid is not None:
        vid.download(filepath)
        print("Download is completed successfully")
    else:
        print("Encountered error")


# asking for input
link = input("Enter the YouTube video/playlist URL: ")
filepath = input("Enter the file path for where the video should be downloaded: ")

# Checks if url is a playlist URL or a video URL
error_occured = False
video_url = ""
try:
    playlist = Playlist(link)
    video_url = playlist.video_urls
    print(video_url)
except Exception:
    error_occured = True

# Downloads video(s)
if error_occured:
    download(link, filepath)
else:
    for i in range(0, len(video_url)):
        link = video_url[i]
        print("Downloading - ", YouTube(link).title)
        download(link, filepath)
    print("Downloads completed")
