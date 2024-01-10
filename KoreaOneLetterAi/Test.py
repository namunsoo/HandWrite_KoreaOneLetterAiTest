# -*- coding:utf-8 -*-

import numpy as np
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == "__main__":
    
    data = np.array([[i] for i in range(100)])
    target = np.array([i+1 for i in range(1, 101)])
    data = np.reshape(data, (100, 1, 1))
    
    model = Sequential([
        layers.Bidirectional(layers.LSTM(64, return_sequences=True), input_shape=(1, 1)),
        layers.Bidirectional(layers.LSTM(32)),
        layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')
   
    model.summary()
    
    model.fit(data, target, epochs=10, batch_size=1)