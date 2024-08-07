from pytube import YouTube

def download_mp4():
    pass

def download_mp3():
    pass

def download_playlist(instruction):
    if instruction == "mp3":
        #for jedes video download es
        pass
    else:
        # download mp4
        pass
    pass

yt = YouTube("https://youtu.be/xcfft9RCM6I?feature=shared")
#stream = yt.streams.get_highest_resolution()
stream = yt.streams
stream.download("ytplaylistdownload/test.mp4")
print('Download completed: ')