在空间上对视频进行切割。

* 首先，提取出yuv的每一帧图像，保存成png。（注：png是无损压缩，jpg是有损的，所以要用png格式）

	命令：

	```
ffmpeg -s 4096x2048 -i Hangpai_2.yuv -r 30 image2 Hangpai_2_req_%d.png
```

* 然后用 **videoSegmentation.py** 对每张图片进行空间上的8x8切片

* 最后用ffmpeg把图片拼成视频。

	命令：
	
	```
	ffmpeg -r 30 -i Hangpai_2_req_seg_seg_1_%d.png -c:v libx264 -y out.mp4
	```

结果...未完待续...