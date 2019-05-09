# * coding:utf-8 *
"""
@Author: GRYun
@Date  : 19-5-8
@Time  : 下午2:34
@File  : dataload.py
@IDE   : PyCharm
@Func  :
"""

import os
import re

"""
process the moive 
load the dir
the moive filter

"""
class dataload:
    def __init__(self,path):
        self.path = path

    # read the file name in the dir
    # only a foolr dir
    def file_name(self,path):
        list_name = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.splitext(file)[1] == '.bmp':
                    list_name.append(file)
        return list_name

    # read the file name in the dir
    # can use sub dir
    def listdir(self,path):
        list_name = []
        for files in os.listdir(path):
            file_path = os.path.join(path, files)
            if os.path.isdir(file_path):
                self.listdir(file_path)
            elif os.path.splitext(file_path)[1] == '.bmp':
                list_name.append(file_path)
        return list_name

    # get the image belong to the video
    def getfilmno(self,fname):
        pattern = re.compile(r"(?<=_).*?(?=_)", re.I);
        matcher = pattern.findall(fname)
        return matcher[0]

    # total the video has frame
    def videoframe(self,file_list):
        moive_no = {}
        for row in file_list:
            v_no = self.getfilmno(self,row)
            if v_no in moive_no.keys():
                moive_no[v_no] += 1
            else:
                moive_no[v_no] = 1
        return moive_no