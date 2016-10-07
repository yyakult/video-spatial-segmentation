import cv2
import os

# Pictures Parameters
PICTURES_PREFIX = "Hangpai_2_req_"
PICTURES_FORMAT = ".png"
PICTURES_NUM = 360

# Segmentation Parameters
NUM_W = 8
NUM_H = 8
W = 4096
H = 2048 
SEGMENT_W = W / NUM_W
SEGMENT_H = H / NUM_H

# Output Parameters
FLODER_NAME = "seg_"
OUTPUT_PICTURES_PREFIX = PICTURES_PREFIX+"seg_"
OUTPUT_PICTURES_FORMAT = ".png"

for i in range(1,NUM_W*NUM_H+1):
	os.mkdir(FLODER_NAME+str(i))


for n in range(1,PICTURES_NUM+1):
	img_name = PICTURES_PREFIX+str(n)+PICTURES_FORMAT
	print img_name
	img = cv2.imread(img_name)
	for i in range(1,NUM_H+1):
		for j in range(1,NUM_W+1):
			img_seg = img[SEGMENT_H*(i-1):SEGMENT_H*(i), SEGMENT_W*(j-1):SEGMENT_W*(j)]
			folder = FLODER_NAME + str((i-1)*NUM_H+j)
			cv2.imwrite(folder+"/"+OUTPUT_PICTURES_PREFIX+str(folder)+"_"+str(n)+OUTPUT_PICTURES_FORMAT, img_seg)


	