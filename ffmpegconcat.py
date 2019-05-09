# * coding:utf-8 *
"""
@Author: GRYun
@Date  : 19-5-8
@Time  : 下午2:33
@File  : ffmpegconcat.py
@IDE   : PyCharm
@Func  :
"""
import os

from dataload import dataload as load

video_dir = "/home/han/Desktop/video/"
file_list = load.file_name(load,video_dir)
movie_list_num = load.videoframe(load,file_list)
print(movie_list_num)
for key ,value in movie_list_num.items():
    iname = video_dir+"Youku_" + key + "_l"
    oname = video_dir+"Youku_" + key + "_res"
    # im_name = os.path.join(video_dir, "Youku_" + key + "_l" + str(i + 1).zfill(3) + ".bmp")
    com1 = "ffmpeg -i "+ iname +"%3d.bmp  -pix_fmt yuv420p  -vsync 0 "+oname+".y4m -y"
    os.system(com1)