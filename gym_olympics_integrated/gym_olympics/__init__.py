from gym.envs.registration import register

# # olympics running env with the same map, map id can be specified as
# # gym.make('gym_olympics:running-v0', map_id=1)
# register(
#     id='running-v0',
#     entry_point='d4rl.gym_olympics.envs:running',
#     max_episode_steps=400,
# )

# # olympics running env with map changing randomly
# # gym.make('gym_olympics:rd_running-v0')
# register(
#     id='rd_running-v0',
#     entry_point='d4rl.gym_olympics.envs:rd_running',
#     max_episode_steps=400,
# )

# # gym.make('gym_olympics:table_hockey-v0')
# register(
#     id='table_hockey-v0',
#     entry_point='d4rl.gym_olympics.envs:table_hockey',
#     max_episode_steps=400,
# )

# # gym.make('gym_olympics:football-v0')
# register(
#     id='football-v0',
#     entry_point='d4rl.gym_olympics.envs:football',
#     max_episode_steps=400,
# )

# # gym.make('gym_olympics:wrestling-v0')
# register(
#     id='wrestling-v0',
#     entry_point='d4rl.gym_olympics.envs:wrestling',
#     max_episode_steps=400,
# )

# ALL_ENVS = [
#     'jidi-olympics-running-expert-v0',
#     'jidi-olympics-rd_running-expert-v0',
#     'jidi-olympics-table_hockey-expert-v0',
#     'jidi-olympics-football-expert-v0',
#     'jidi-olympics-wrestling-expert-v0',
# ]

ALL_ENVS = [
    'jidi-olympics-running-v0',
    'jidi-olympics-rd_running-v0',
    'jidi-olympics-table-hockey-v0',
    'jidi-olympics-football-v0',
    'jidi-olympics-wrestling-v0',
    'jidi-olympics-curling-v0',
    'jidi-olympics-billiard-v0',
    'jidi-olympics-integrated-v0',
]

for env in ALL_ENVS:
    register(
        id=env,
        entry_point='gym_olympics.envs:OlympicsEnv',
        kwargs={
            'game': env,
        }
    )

