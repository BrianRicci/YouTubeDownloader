from pytube import *


# print(yt.title) # название видео
# print(yt.thumbnail_url) # превью


def main():
    yt = YouTube('https://youtube.com/watch?v=CZPeXX6t1no')

    
    
    # video = yt.streams.get_by_resolution('720p') # выбор разрешения и пути сохранения видео

    # video.download()

if __name__ == "__main__":
    main()