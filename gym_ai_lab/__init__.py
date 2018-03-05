from gym.envs.registration import register

register(
    id='SmallMaze-v0',
    entry_point='gym_ai_lab.envs:SmallMazeEnv')
register(
    id='GrdMaze-v0',
    entry_point='gym_ai_lab.envs:GrdMazeEnv')
