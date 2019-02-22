from slugify import slugify
import cv2, pafy, os, time

print("Enter the url of playlist:")
plurl=input()
start_time = time.time()

def mycb(total, recvd, ratio, rate, eta):
    print(total, recvd*100/total, ratio, eta)


playlist = pafy.get_playlist(plurl)
print('No of items in playlist = '+str(len(playlist['items'])))
for v in playlist['items']:
    vid = v['pafy']
    print("Title -----------:" +vid.title)
    bestA = vid.getbestaudio(preftype="m4a")
    musicFile = slugify(vid.title)+'.m4a'
    if (os.path.exists(musicFile)):
        os.remove(musicFile)
    bestA.download(filepath=musicFile,quiet=True,callback=mycb)

print("--- %s minutes ---" % (time.time() - start_time)/60)


             
