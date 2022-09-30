import gym
import gym_olympics
import numpy as np

all_levels = gym_olympics.ALL_ENVS

for env_name in all_levels:
    print(env_name)
    env_name = 'jidi-olympics-curling-v0'
    env = gym.make(env_name, map_idx=3)
    for i in range(2):
        obs = env.reset()
        env.render()
        ep_step = 0
        while True:
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            assert obs is not None
            env.render()
            ep_step += 1
            if done:
                ep_step = 0
                break

    env.close()
    print(f'level {env_name} passed')