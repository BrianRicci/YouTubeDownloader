import os
import eel
from pytube import YouTube

eel.init('web')


@eel.expose
def downloader(URL, res):
    yt = YouTube(URL)
    
    video = yt.streams.filter(mime_type='video/mp4', only_video=True)
    video = video[int(res)]

    backslash = '\\'
    video.download(output_path=f'{os.getcwd().replace(backslash, "/")}/downloads')    
    

@eel.expose
def getInfo(URL):
    yt = YouTube(URL)
    
    video = yt.streams.filter(mime_type='video/mp4', only_video=True)
    resolution_list = [res.resolution for res in video]
    size_list = [format(size.filesize_mb, '.2f') for size in video]

    video_info = {
        "title": yt.title,
        "preview": yt.thumbnail_url,
        "sizes": size_list,
        "resolutions": resolution_list
    }
    return video_info

@eel.expose
def open_folder():
    backslash = '\\'
    path = f'{os.getcwd().replace(backslash, "/")}/downloads'
    
    if os.path.isdir(path):
        os.startfile(path)
    else:
        os.mkdir(path)
        os.startfile(path) 

eel.start('main.html', size=(500, 800), block=True)

