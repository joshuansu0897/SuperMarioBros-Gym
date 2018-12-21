import gym
import ppaquette_gym_super_mario

env = gym.make('ppaquette/SuperMarioBros-1-1-v0')
observation = env.reset()
done = False
t = 0
while not done:
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    t += 1
    if not t % 100:
        print(t, info)
