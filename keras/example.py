import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# модель из последовательности слоев
model = Sequential()

# добавляем слои
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# настройки обучения
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
# пример расширения настройки (через наследование)
# model.compile(
#     loss=keras.losses.categorical_crossentropy,
#     optimizer=keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
# )

# данные
x_train = np.array([[1], [2]])
y_train = np.array([[5], [10]])
x_test = np.array([[3], [4]])
y_test = np.array([[15], [20]])

# обучение
model.fit(x_train, y_train, epochs=5, batch_size=32)

# проверка качества обучения
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)
print(loss_and_metrics)

# ИЛИ генерация прогноза на новых данных
classes = model.predict(x_test, batch_size=128)
print(classes)
