# -*- coding:utf-8 -*-

import numpy as np
import PIL
import tensorflow as tf

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
    
    directory = 'C:\\Users\\namunsoo\\Downloads\\AI_Data\\OneLetter'
    img_width = 56
    img_height = 56
    batch_size = 1024
    train_ds, val_ds = keras.utils.image_dataset_from_directory(
        directory,
        color_mode='grayscale', # 이미지 전처리
        batch_size=batch_size, # 한번에 학습시킬 양
        image_size=(img_height, img_width),
        shuffle=True, # 데이터 섞을지 여부 기본값 false
        seed=123, # 섞을때 시드 (만약 데이터를 다시 섞을경우에도 같은 값이면 섞은 결과도 같음)
        validation_split=0.2, # (subset both 일 경우만 사용) 전체의 20%를 확인용으로 사용
        subset="both", # 데이터 학습용인지 확인용인지 또는 둘다인지
        crop_to_aspect_ratio=True # 이미지 가져올때 종횡비
    )

    outPut = len(train_ds.class_names)

    model = Sequential([
        layers.Rescaling(1./255, input_shape=(img_width, img_height, 1)),
        layers.Conv2D(48, (3, 3), activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(96, (3, 3), activation='relu'),
        layers.MaxPooling2D(),
        layers.Dropout(0.2),
        layers.Flatten(),
        layers.Dense(outPut)
    ])

    model.compile(optimizer=keras.optimizers.Adam(),
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=[keras.metrics.SparseCategoricalAccuracy()])
   
    model.summary()
    
    # model = keras.models.load_model('my_model_epochs_1.keras')
    for i in range(1,16):
        model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=1
        )
        model.save('my_model_epochs_'+str(i)+'.keras')