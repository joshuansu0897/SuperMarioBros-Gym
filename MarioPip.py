from nes_py.wrappers import BinarySpaceToDiscreteSpaceEnv
import gym_super_mario_bros

from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

env = gym_super_mario_bros.make('SuperMarioBrosNoFrameskip-1-1-v0')
env = BinarySpaceToDiscreteSpaceEnv(env, SIMPLE_MOVEMENT)

for _ in range(1000):
    observation = env.reset()
    done = False
    t = 0
    while not done:
        observation, reward, done, info = env.step(env.action_space.sample())
        env.render()
        t += 1
        if not t % 100:
            print(t, info)

env.close()