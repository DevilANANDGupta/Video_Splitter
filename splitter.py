
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# Replace the filename below.

required_video_file = "V2.mkv"
with open("times.txt") as f:
  times = f.readlines()
times = [x.strip() for x in times] 
for time in times:
  starttime = int(time.split("-")[0])
  endtime = int(time.split("-")[1])
  ffmpeg_extract_subclip(required_video_file, starttime, endtime, targetname=str(times.index(time)+1)+".mkv")
