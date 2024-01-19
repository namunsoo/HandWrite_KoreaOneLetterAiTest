# -*- coding:utf-8 -*-

import codecs
import shutil
import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == "__main__":
    
    # common = AI_Common.Common('C:\\Users\\namunsoo\\Downloads\\AI_Data\\Label\\printed_data_info.json')

    jsonData = None
    imageFolder = 'C:\\Users\\namunsoo\\Downloads\\AI_Data\\OneLetter\\'
    jsonData = 'C:\\Users\\namunsoo\\Downloads\\AI_Data\\handwriting_data_info_clean.json'
    bytesEncoded = None
    textUnicode = None
    byteArray = None
    folderName = None
    count = 0;
    with open(jsonData, 'r', encoding='UTF8') as f:
        jsonData = json.load(f)
        for item in jsonData['annotations']:
            if item['attributes']['type'] == '글자(음절)':
                
                # # 초성
                # textUnicode = ord(item['text'])
                # folderName = str(int(((textUnicode - 0xAC00) / 28) / 21))
                
                # # 중성
                # textUnicode = ord(item['text'])
                # folderName = str(int(((textUnicode - 0xAC00) / 28) % 21))
                
                # 종성
                textUnicode = ord(item['text'])
                folderName = str(int((textUnicode - 0xAC00) % 28))
                
                # # keras image_dataset_from_directory 여기서 한글 인식 못함
                # bytesEncoded = item['text'].encode(encoding='utf-8')
                # byteArray = list(bytesEncoded)
                # folderName = ','.join(str(e) for e in byteArray)
                
                # 폴더 있으면 옴기기만 없으면 생성후 옴기기
                if os.path.isdir(imageFolder+folderName):
                    shutil.move(imageFolder+item['id']+'.png', imageFolder+folderName+'\\'+item['id']+'.png')
                else:
                    os.mkdir(imageFolder+folderName)
                    shutil.move(imageFolder+item['id']+'.png', imageFolder+folderName+'\\'+item['id']+'.png')
                    
                count += 1
                if count % 1000 == 0:
                    print(count)
