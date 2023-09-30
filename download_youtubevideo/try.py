import youtube_dl

video_url = "https://www.youtube.com/watch?v=uqq7Fv3Op4U"

options = {
    'writesubtitles': True,
    'subtitleslangs': ['tr'],  # İndirmek istediğiniz altyazı dilini belirleyin
    'skip_download': True,  # Sadece altyazıları indir, videoyu indirme
    'subtitlesformat': 'vtt',  # Altyazı formatı (vtt, srt, ttml, vb.)
    'outtmpl': '%(id)s.%(ext)s',  # İndirilen altyazı dosyasının adı
}

with youtube_dl.YoutubeDL(options) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    ydl.download([video_url])
    subtitles = ydl.get_subtitles(info_dict)

if subtitles:
    for lang, subs in subtitles.items():
        for sub in subs:
            print(f"Subtitle language: {lang}")
            print(f"Subtitle content:\n{sub['data']}\n")
else:
    print("No subtitles found for the video.")
