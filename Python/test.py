import tensorflow as tf

# 下载并加载 MNIST 数据集
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 创建一个包含1000个样本的小型数据集
small_X_train = X_train[:1000]
small_y_train = y_train[:1000]

print(small_X_train.shape, small_y_train.shape)
