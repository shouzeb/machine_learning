# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 01:16:35 2020

@author: Shouzeb
"""

import tensorflow as tf
import numpy as np

celsius_q    = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)

model = tf.keras.Sequential([
tf.keras.layers.Dense(units=1, input_shape=[1])
])
model.compile(loss='mean_squared_error',
              optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Finished training the model")
import matplotlib.pyplot as plt
plt.xlabel('Epoch Number')
plt.ylabel("Loss Magnitude")
plt.plot(history.history['loss'])
print(model.predict([101]))
