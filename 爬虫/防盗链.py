# Refere

import requests

url2 = 'https://www.pearvideo.com/video_1679488'

contId = url2.split('_')[1]

url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1679488&mrd=0.43370401633001276'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
'Referer': 'https://www.pearvideo.com/video_1679488'
}



res = requests.get(url=url, headers=headers)

a = res.json()['videoInfo']['videos']['srcUrl']

b= res.json()['systemTime']

srcurl = a.replace(b,f"cont-{contId}")
print(srcurl)

with open('a.mp4',mode='wb') as f:
    f.write(requests.get(srcurl).content)




