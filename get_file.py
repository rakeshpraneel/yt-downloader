from yt_dlp import YoutubeDL


def download_video():
    URLS = [""]
    save_path = "output/"
    yt_opts = {
        'paths': {
                'home': save_path
            },
    }
    with YoutubeDL(yt_opts) as ydl:
        ydl.download(URLS)