import os

for i in range(1,65):
	print i
	command = "ffmpeg -r 30 -i seg_"+str(i)+"/Hangpai_2_req_seg_"+str(i)+"_%d.png -c:v libx264 -y video_seg_norestrictions/"+str(i)+".mp4 2> video_seg_norestrictions/log/"+str(i)+".txt"
	os.system(command)
