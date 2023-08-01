from pytube import *
import os


# print(yt.title) # название видео
# print(yt.thumbnail_url) # превью
# print(video[0].filesize_mb)

def open_folder():
    backslash = '\\'
    path = f'{os.getcwd().replace(backslash, "/")}/downloads'
    
    if os.path.isdir(path):
        os.startfile(path)
    else:
        os.mkdir(path)
        os.startfile(path)


def main():
    # yt = YouTube('https://youtube.com/watch?v=CZPeXX6t1no')

    # video = yt.streams.filter(mime_type='video/mp4', only_video=True)
    # video = video[3]
    # resolution_list = [res.resolution for res in video]
    # sizes = [format(size.filesize_mb, '.2f') for size in video]
    # print(sizes)
    # for i in video:
    #     print(i)
    # backslash = '\\'
    # video.download(output_path=f'{os.getcwd().replace(backslash, "/")}/downloads')    
    open_folder()


if __name__ == "__main__":
    main()