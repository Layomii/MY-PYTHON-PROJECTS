from pytube import YouTube

link = input("https://www.youtube.com/watch?v=jG4zCt4Nlis")
yt = YouTube("https://www.youtube.com/watch?v=jG4zCt4Nlis")


print("Title: CAMERAMAN", yt.title)
print("Number of views: 60,758,975", yt.views)
print("Lenghth of video: 23", yt.length)

ys = yt.streams.get_highest_resolution()

print("Downloading...")
ys.download()
print("Download!!!")