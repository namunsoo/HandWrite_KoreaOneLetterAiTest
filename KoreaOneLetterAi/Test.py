# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf
import cv2

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

# 오류 제거
# (선능을 높일수 있다 어쩌구 저쩌구)
# this tensorflow binary is optimized to use available cpu instructions in performance-critical operations.
# 이 텐서플로우 바이너리는 성능이 중요한 작업에서 사용 가능한 CPU 명령을 사용하도록 최적화되어 있습니다.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == "__main__":
    # # 0, 19, 6
    # textUnicode = ord('뷔')
    # result = 0xAC00 + (0 * 21 * 28) + (0 * 28) + 0
    # # result_to_byte = result.to_bytes(2, byteorder='big')
    # # result_to_byte = bytes(0xAC00)
    # print(int(((textUnicode - 0xAC00) / 28) / 21))
    # print(int(((textUnicode - 0xAC00) / 28) % 21))
    # print(int((textUnicode - 0xAC00) % 28))
    
    test_image = cv2.imread('test3.png', cv2.IMREAD_GRAYSCALE)
    test_image = cv2.resize(test_image, (56,56), interpolation = cv2.INTER_AREA)
    
    first_model = keras.models.load_model('my_model_korea_first_ep15.keras')
    second_model = keras.models.load_model('my_model_korea_second_ep15.keras')
    last_model = keras.models.load_model('my_model_korea_last_ep15.keras')
        
    first = first_model.predict(test_image.reshape(1,56,56,1))
    second = second_model.predict(test_image.reshape(1,56,56,1))
    last = last_model.predict(test_image.reshape(1,56,56,1))
    
    # first = first_model.predict(np.expand_dims(test_image, axis=0))
    # second = second_model.predict(np.expand_dims(test_image, axis=0))
    # last = last_model.predict(np.expand_dims(test_image, axis=0))
    
    # print(first[0])
    # print(second[0])
    # print(last[0])

    # print(np.argmax(first[0]))
    # print(np.argmax(second[0]))
    # print(np.argmax(last[0]))
    
    # aaaa = (int)(np.argmax(first))
    # bbbb = (int)(np.argmax(second))
    # cccc = (int)(np.argmax(last))
    # print(aaaa)
    # print(bbbb)
    # print(cccc)
    
    result = 0xAC00 + ((int)(np.argmax(first)) * 21 * 28) + ((int)(np.argmax(second)) * 28) + (int)(np.argmax(last))
    print(chr(result))
    
    # result = 0xAC00 + (10 * 21 * 28) + (9 * 28) + 0
    # print(chr(result))