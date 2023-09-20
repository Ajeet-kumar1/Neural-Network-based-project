
import pytube
import numpy as np
def downloader(link, storing_path):
    # Link should be in standard ID format
    # Exmple : https://www.youtube.com/watch?v=AJEETKUMARY
    vid_id = link[-12:]
    # print(vid_id)
    yt = pytube.YouTube(link)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    filename1 = storing_path+"/"+vid_id+".mp4"
    stream.download(filename=filename1)
    return vid_id


############## Driver code #################################################
storing_path = "/home/ba-ajeetkumary/SYMON_New/SYMON/Videos"
# Now make one npz file and store all the video IDs which are getting download
downloaded_ids = []
with open("/home/ba-ajeetkumary/SYMON_New/SYMON/url2.txt") as f:
    for line in f:
        video_url = str(line)
        try:
            vid_id = downloader(video_url, storing_path)
            downloaded_ids.append(vid_id)
        except:
            NameError
# Store the IDs of all downloaded videos.
np.savez_compressed("/home/ba-ajeetkumary/SYMON_New/Dummy2.npz", downloaded_ids)
