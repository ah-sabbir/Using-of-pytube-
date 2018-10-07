from pytube import YouTube
import os
'''
Author by Ahmmed Sabbir
'''
def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()# it can changed res="your own resulations" 
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
link_list=["https://www.youtube.com/watch?v={place here video ID}"]#this is the video link list.. replace the video link which will be downloaded

try:
	print("start download")
	for link in link_list:

		downloadYouTube(link,'C:\\Users\\User\\Videos\\movies')#this is download folder path that you can change 
		print("completed !!!")
except:
	print("problem .... downloading failed")


