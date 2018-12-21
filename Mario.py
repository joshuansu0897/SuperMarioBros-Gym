import gym
import ppaquette_gym_super_mario
import numpy as np

env = gym.make('ppaquette/SuperMarioBros-1-1-v0')

observation = env.reset()
done = False
t = 0
while not done:
    action = np.random.randint(2, size=6)
    observation, reward, done, info = env.step(action)
    t += 1
    if not t % 100:
        print(t, info)