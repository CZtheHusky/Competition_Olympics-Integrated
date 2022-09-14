import gym
import gym_olympics
import numpy as np

all_levels = gym_olympics.ALL_ENVS

for env_name in all_levels:
    env_name = 'jidi-olympics-rd_running-v0'
    print(env_name)
    env = gym.make(env_name, map_idx=3)
    for i in range(2):
        obs = env.reset()
        env.render()
        ep_step = 0
        while True:
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            env.render()
            ep_step += 1
            if done:
                if 'curling' in env_name or 'billiard' in env_name:
                    print('No max step limit')
                    pass
                else:
                    print('Max step limit passed')
                    assert ep_step <= 400
                ep_step = 0
                break

    env.close()
    print(f'level {env_name} passed')