## How to use

`pip install -e gym_olympics_integrated`

# Competition_Olympics-Integrated
---
## Updates:

**05/05/2022**: We fix some bugs, extend episode length of each subgames and add side information to the output information, including the partially-observed array, the energy left and the NEW_GAME Flag hinting the switch of subgames; we also shift agent's view backward, letting the agent to see its back and the whole body of the agent itself as well. Meanwhile, we randomly shuffle the order of subgames.

rl_trainer is added, serving as an example on how to train an RL agents.

---
## Environment

<img src=https://github.com/jidiai/Competition_Olympics-Integrated/blob/main/olympics_engine/assets/multi-task-olympics.gif width=600>


Check details in Jidi Competition [IJCAI-ECAI 2022 AI Qlympics Competition](http://www.jidiai.cn/compete_detail?compete=17) and [WAIC 2022 AI Qlympics Competition](http://www.jidiai.cn/compete_detail?compete=18)


### Olympics-Integrated
<b>Tags</b>Partial Observation; Continuous Action Space; Continuous Observation Space

<b>Introduction: </b>Agents participate in the Olympic Games. In this series of competitions, two agents participate in different Olympics games, including running, football, table hockey, wrestling etc.

<b>Environment Rules:</b> 
1. This game has two sides and both sides control an elastic ball agent with the same mass and radius.
2. Agents can collide with each other or walls, but they might lose a certain speed. The agent has its own energy, and the energy consumed in each step is directly proportional to the applied driving force and displacement.
3. The energy of the agent recovers at a fixed rate at the same time. If the energy decays to zero, the agent will be tired, resulting in failure to apply force.
4. The whole game contains the subgames below. In running, the goal is to reach the end as fast as possible. In football, agent needs to hit the ball through collision into opponent's goal and defend his own goal. In table-hockey, agents share the same objective as in football except that they can only move freely in our own half court. In wrestling, agent who knock others out of bounds while keeping staying in bounds wins the game.
5. The game ends when all subgames are finished.


<b>Action Space: </b>Continuous, a matrix with shape 2*1, representing applied force and steering angle respectively.

<b>Observation: </b>A dictionary with keys 'obs' and 'controlled_player_index'. The value of 'obs' contains a 2D matrix with shape of 40x40 and other game-releated infomation. The 2D matrix records the view of agent along his current direction. Agent can see walls, marking lines, opponents and other game object within the vision area. The value of 'controlled_player_index' is the player id of the game. The side information includes energy left and a game-switching flags.

<b>Reward: </b>Each team obtains a +1 reward when winning a subgame, and 0 reward when losing a subgame.

<b>Environment ends condition: </b>The game ends when all subgames are finished.

<b>Registration: </b>Go to (http://www.jidiai.cn/compete_detail?compete=17 and http://www.jidiai.cn/compete_detail?compete=18).


---
## Dependency

>conda create -n olympics python=3.8.5

>conda activate olympics

>pip install -r requirements.txt

---

## Run a game

>python olympics_engine/main.py

---

## How to test submission

You can locally test your submission. At Jidi platform, we evaluate your submission as same as *run_log.py*

For example,

>python run_log.py --my_ai "random" --opponent "random"

in which you are controlling agent 1 which is green.

---

## Ready to submit

Random policy --> *agents/random/submission.py*
