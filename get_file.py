from yt_dlp import YoutubeDL

URLS = []
save_path = "output/"
yt_opts = {
    'paths': {
            'home': save_path
        },
}
with YoutubeDL(yt_opts) as ydl:
    ydl.download(URLS)