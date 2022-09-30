import gym
from pathlib import Path
import sys
CURRENT_PATH = str(Path(__file__).resolve().parent)
sys.path.append(CURRENT_PATH)
import numpy as np
from gym import spaces
from olympics_env.olympics_integrated import OlympicsIntegrated
import os
import json


class OlympicsEnv(gym.Env):
    def __init__(self,
                 game, map_idx=None, max_episode_steps=400,
                 **kwargs) -> None:
        super().__init__()
        config_path = os.path.join(os.path.dirname(__file__), 'olympics_env', 'config.json')
        with open(config_path) as f:
            conf = json.load(f)['olympics-integrated']
        env = OlympicsIntegrated(conf, game, map_idx=map_idx, max_episode_steps=max_episode_steps, **kwargs)
        self._env = env
        # self.post_process_fn = post_process
        self.action_space = spaces.Box(low=-1, high=1, shape=(2, 2), dtype=np.float32)
        self.observation_space = spaces.Box(0, 255., shape=(2, 1602), dtype=np.float32)
        # self.observation_space = spaces.Dict({
        #     'obs': spaces.Box(0, 255, shape=(2, 40, 40), dtype=np.uint8),
        #     'energy': spaces.Box(0, 1, shape=(2, ), dtype=np.float32),
        #     'new_game': spaces.Box(0, 1, shape=(2, ), dtype=np.uint8),
        # })
        self.new_game_mapper = {'NEW GAME': 1, '': 0}

    def step(self, action):
        obs, reward, done, info_before, info_after = self._env.step(self.action_mapper(action))
        return self.obs_wrapper(obs), reward, done, {}

    def reset(self, **kwargs):
        obs = self._env.reset()
        return self.obs_wrapper(obs)

    def render(self, **kwargs):
        self._env.env_core.render()

    def seed(self, seed=None):
        self._env.seed(seed)

    def obs_wrapper(self, obs):
        if obs is None:
            return obs
        obs = [obs[0]['obs'], obs[1]['obs']]
        array_obs = [obs[0]['agent_obs'].flatten(), obs[0]['agent_obs'].flatten()]
        game_mode = [self.new_game_mapper[obs[0]['game_mode']], self.new_game_mapper[obs[1]['game_mode']]]
        energy = [obs[0]['energy'] / 1000, obs[1]['energy'] / 1000]
        obs = np.array([np.hstack([array_obs[0], game_mode[0], energy[0]]), np.hstack([array_obs[1], game_mode[1], energy[1]])], dtype=np.float32)
        # print(obs.shape)
        return obs

    def action_mapper(self, action):
        # action_f = [-100, 200]
        # action_theta = [-30, 30]
        # map action of [-1, 1] to [-100, 200] and [-30, 30]
        action[:, 0] = action[:, 0] * 150. + 50.
        action[:, 1] = action[:, 1] * 30.
        action = [[[action[0][0]], [action[0][1]]], [[action[1][0]], [action[1][1]]]]
        # print(action)
        return action

    def inverse_act_mapper(self, action):
        action[:, 0] = (action[:, 0] - 50) / 150
        action[:, 1] = action[:, 1] / 30
        # print(action)
        return action
