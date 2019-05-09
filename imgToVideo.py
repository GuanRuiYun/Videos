# * coding:utf-8 *
"""
@Author: GRYun
@Date  : 19-5-8
@Time  : 上午9:20
@File  : imgToVideo.py
@IDE   : PyCharm
@Func  : The images concat video
"""

import cv2
import os
import re

# read the file name in the dir
# only a foolr dir
def file_name(file_dir):
    list_name = []
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.bmp':
                list_name.append(file)
    return list_name

# read the file name in the dir
# can use sub dir
def listdir(path):
    list_name = []
    for files in os.listdir(path):
        file_path = os.path.join(path,files)
        if os.path.isdir(file_path):
            listdir(file_path)
        elif os.path.splitext(file_path)[1] == '.bmp':
            list_name.append(file_path)
    return list_name


# get the image belong to the video
def getfilmno(fname):
    pattern = re.compile(r"(?<=_).*?(?=_)", re.I);
    matcher = pattern.findall(fname)
    return matcher[0]

# total the video has frame
def videoframe(file_list):
    moive_no = {}
    for row in file_list:
        v_no = getfilmno(row)
        if v_no in moive_no.keys():
            moive_no[v_no] += 1
        else:
            moive_no[v_no] = 1
    return moive_no


video_dir = "/home/han/Desktop/video"
file_list = file_name(video_dir)
movie_list_num = videoframe(file_list)
# print(movie_list_num)

# 图片路径
im_dir = '/home/han/Desktop/video'
#输出视频路径
video_dir = '/home/han/Desktop/video/out/output_'
#帧率
fps = 25
#图片数
num = 426
#图片尺寸
img_size = (480,270)

#fourcc = cv2.cv.CV_FOURCC('M','J','P','G')#opencv2.4
# fourcc = cv2.VideoWriter_fourcc('X','2','6','4') #opencv3.0
fourcc = cv2.VideoWriter_fourcc('M','J','P','G') #opencv3.0

for key ,value in movie_list_num.items():

    videoWriter = cv2.VideoWriter(video_dir+key+'_Res.avi', fourcc, fps, img_size)
    for i in range(0, value):
        im_name = os.path.join(im_dir, "Youku_" + key + "_l"+str(i+1).zfill(3)+ ".bmp")
        frame = cv2.imread(im_name)
        videoWriter.write(frame)

    videoWriter.release()
    print('finish:=> ',video_dir+key+'_Res.avi')
    dir = str(video_dir + key + '_Res.avi').strip(".avi")
    commond = "ffmpeg -i %s.avi -vsync 0 %s.y4m -y" % (dir,dir)
    os.system(commond)
    # commond1 = "ffmpeg -s 1920x1080 -i %s.yuv -vsync 0 %s.y4m -y"% (dir,dir)
    # os.system(commond1)
print('finish')

"""



print('finish')
"""

"""

res2 = listdir(video_dir)
key = "Youku_00000_l053.bmp"
pattern = re.compile(r"(?<=_).*?(?=_)",re.I);
matcher = pattern.findall(key)
print(matcher[0])

moive_no = {}
for row in file_list:
    v_no = getfilmno(row)
    if v_no in moive_no.keys():
        moive_no[v_no] += 1
    else:
        moive_no[v_no] = 1
print(moive_no)

"""