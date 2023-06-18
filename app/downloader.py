from pytube import *


# print(yt.title) # название видео
# print(yt.thumbnail_url) # превью

def get_video_resolutions(yt):
    video = yt.streams.filter(file_extension='mp4')

    resolutions = set()

    for res in video:
        resolutions.add(res.resolution)

    resolutions.discard(None)
    resolutions = sorted(resolutions)
    
    return resolutions

def main():
    yt = YouTube('https://youtube.com/watch?v=CZPeXX6t1no')

    print(get_video_resolutions(yt))
    
    # video = yt.streams.get_by_resolution('720p') # выбор разрешения и пути сохранения видео

    # video.download()

if __name__ == "__main__":
    main()