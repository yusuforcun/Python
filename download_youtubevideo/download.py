# # from pytube import YouTube

# # yt = YouTube('https://www.youtube.com/watch?v=fwFX24MSBp4&list=RDfwFX24MSBp4&start_radio=1') #video link

# # # print(f"Video Başlığı: {yt.title}")
# # print(f"Video Sahibi: {yt.author}")
# # print(f"Thumbnail Resmi: {yt.thumbnail_url}")
# # print(f"Video Uzunluğu: {yt.length}")
# # print(f"Video Rating: {yt.rating}")
# # # print(f"İzlenme Sayısı: {yt.views}")
# # print("*"*30)
# # # print(f"Video Açıklaması: {yt.description}")
# # print("*"*30)


# -------------------------------------------

# from pytube import YouTube

# yt = YouTube('https://www.youtube.com/watch?v=qolmz4FlnZ0')

# for i in yt.streams:
#     print(i)

# -------------------------------------------

from pytube import YouTube

# Videoyu indirmek için YouTube URL'sini belirtin
video_url = "https://yabancidizi.pro/dizi/how-i-met-your-mother-izle-6/sezon-1/bolum-1"
def  download():
    # YouTube nesnesi oluşturun ve videoyu indirin
    yt = YouTube(video_url)
    desired_resolution = '720p'  # İstenen çözünürlükü buraya girin
    
    # video = yt.streams.filter(res=desired_resolution).first()
    video = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    video.download()
download()