# -*- coding:utf-8 -*-

import codecs
import shutil
import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == "__main__":
    targetFolder = 'C:\\Users\\namunsoo\\Downloads\\13.한국어글자체\\01.손글씨\\02_handwriting_syllable_images\\2_syllable'
    moveFolder = 'C:\\Users\\namunsoo\\Downloads\\AI_Data\\OneLetter'
    file_list = os.listdir(targetFolder)
    
    count = 0;
    for file in file_list:
        shutil.move(targetFolder+'\\'+file, moveFolder+'\\'+file)
        count += 1
        if count % 1000 == 0:
            print(count)
                