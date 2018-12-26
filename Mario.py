import gym
import ppaquette_gym_super_mario
from keras.models import Sequential
from keras.layers import Dense, Conv2D
from collections import deque
import random
import numpy as np

env = gym.make('ppaquette/SuperMarioBros-1-1-v0')

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=env.observation_space.shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(6, activation='linear', kernel_initializer='uniform'))

D = deque()
observetime = 500
epsilon = 0.7
gamma = 0.9
mb_size = 50

observation = env.reset()

obs = np.expand_dims(observation, axis=0)
state = np.stack((obs, obs), axis=1)

done = False

for t in range (observetime):
    Q = model.predict(state)
    action = np.argmax(Q)
    state, reward, done, info = env.step(action)
    D.append((state, action, reward, state_new, done))
    state = state_new
    if done:
        env.reset()

minibatch = random.sample(D, mb_size)

inputs_shape = (mb_size,) + state.shape[1:]
inputs = np.zeros(inputs_shape)
targets = np.zeros((mb_size, 6))

for i in range(0, mb_size):
    state = minibatch[i][0]
    action = minibatch[i][1]
    reward = minibatch[i][2]
    state_new = minibatch[i][3]
    done = minibatch[i][4]

    inputs[i:i+1] = np.expand_dims(state, axis=0)
    targets[i] = model.predict(state)
    Q_sa = model.predict(state_new)

    if done:
        targets[i, action] = reward
    else:
        targets[i, action] = reward + gamma * np.max(Q_sa)

    model.train_on_batch(inputs, targets)

print('Learning Finished')


observation = env.reset()
obs = np.expand_dims(observation, axis=0)
state = np.stack((obs, obs), axis=1)
done = False
tot_reward = 0.0
while not done:
    Q = model.predict(state)
    action = np.argmax(Q)
    observation, reward, done, info = env.step(action)
    obs = np.expand_dims(observation, axis=0)
    state = np.append(np.expand_dims(obs, axis=0), state[:, :1, :], axis=1)    
    tot_reward += reward
print('Game ended! Total reward: {}'.format(reward))