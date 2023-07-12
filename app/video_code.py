def get_video_code(url):
    if 'list' not in url:
        if 'youtube.com' in url or 'youtu.be' in url:
            return url[-11:]
        else:
            return None
    else:
        code_index = url.index('watch?v=') + 8
        return url[code_index: code_index + 11]
