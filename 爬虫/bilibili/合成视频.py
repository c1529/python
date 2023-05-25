from moviepy.editor import *

url_1 = '《起风了》[我曾难自拔于世间之大，也沉溺于其中梦话].mp3'

url_2 = '《起风了》[我曾难自拔于世间之大，也沉溺于其中梦话].mp4'

video = VideoFileClip(url_2)
audio = AudioFileClip(url_1)
video_merge = video.set_audio(audio)
video_merge.write_videofile('D://1.mp4')


