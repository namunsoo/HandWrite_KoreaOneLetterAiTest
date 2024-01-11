# -*- coding:utf-8 -*-

import codecs
import shutil
import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == "__main__":

    imageFolder = 'C:\\Users\\namunsoo\\Downloads\\AI_Data\\OneLetter'
    file_path = ''
    count = 0
    for filename in os.listdir(imageFolder):
        file_path = os.path.join(imageFolder,filename)
        
        for filelist in os.listdir(file_path):
            # print(filelist)
            shutil.move(file_path+'\\'+filelist, 'C:\\Users\\namunsoo\\Downloads\\AI_Data\\OneLetter\\'+filelist)
            count += 1
            if count % 1000 == 0:
                print(count)
        
        os.rmdir(file_path)