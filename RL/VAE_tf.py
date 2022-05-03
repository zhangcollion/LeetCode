import numpy as  np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow.keras as kr

num_features = 784
epochs = 50
hidden_1 = 128
hidden_2 = 64


def plot_digits(X, y, encoder, batch_size=128):
    z_mean, _, _ = encoder.predict(X)
    plt.figure(figsize=(12, 10))
    plt.scatter(z_mean[:, 0], z_mean[:, 1], c=y)
    plt.colorbar()
    plt.xlabel("z[0] latent dimension")
    plt.ylabel("z[1] latent dimension")
    plt.show()


def sample(args):
    z_mean, z_log_var = args
    eps = tf.random.normal(tf.shape(z_log_var), dtype=tf.float32, mean=0., stddev=1.0, name='epsilon')
    z = z_mean + tf.exp(z_log_var / 2) * eps
    return z


hidden_dim = 512
latent_dim = 2

## encoder
inputs = kr.layers.Input(shape=(num_features,), name="input")
x = kr.layers.Dense(hidden_dim, activation='relu')(inputs)
z_mean = kr.layers.Dense(latent_dim, name='z_mean')(x)
z_log_var = kr.layers.Dense(latent_dim, name='z_log_var')(x)
z = kr.layers.Lambda(sample, name="z")([z_mean, z_log_var])
encoder = kr.Model(inputs, [z_mean, z_log_var, z], name="encoder")

## decoder

latent_inputs = kr.layers.Input(shape=(latent_dim,), name="z_sampling")
x = kr.layers.Dense(hidden_dim, activation="relu")(latent_inputs)
outputs = kr.layers.Dense(num_features, activation='sigmoid')(x)
decoder = kr.Model(latent_inputs, outputs, name='decoder')
decoder.summary()

outputs = decoder(encoder(inputs)[2])
vae = kr.Model(inputs, outputs, name="vae")

reconstruction_loss = tf.losses.mean_squared_error(inputs, outputs)
reconstruction_loss = reconstruction_loss * num_features

kl_loss = 1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var)
kl_loss = -0.5 * tf.reduce_sum(kl_loss, axis=-1)
vae_loss = tf.reduce_mean(reconstruction_loss + kl_loss)
vae.add_loss(vae_loss)
vae.compile(optimizer='adam')
vae.summary()

from tensorflow.keras.datasets import mnist, fashion_mnist


def load_data(choice='mnist', labels=False):
    if choice not in ['mnist', 'fashion_mnist']:
        raise ('Choices are mnist and fashion_mnist')

    if choice is 'mnist':
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
    else:
        (X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

    X_train, X_test = X_train / 255., X_test / 255.
    X_train, X_test = X_train.reshape([-1, 784]), X_test.reshape([-1, 784])
    X_train = X_train.astype(np.float32, copy=False)
    X_test = X_test.astype(np.float32, copy=False)

    if labels:
        return (X_train, y_train), (X_test, y_test)

    return X_train, X_test


## model train
(X_train, _),(X_test, y) = load_data("mnist", labels=True)
vae.fit(X_train, epochs=1, batch_size=32, validation_data=(X_test, None))
plot_digits(X_test, y, encoder)