from gym.envs.registration import register

register(
    id='SmallMaze-v0',
    entry_point='gym_ai_lab.envs:SmallMazeEnv')
register(
    id='GrdMaze-v0',
    entry_point='gym_ai_lab.envs:GrdMazeEnv')
register(
    id='BlockedMaze-v0',
    entry_point='gym_ai_lab.envs:BlockedMazeEnv')

register(
    id='LavaFloor-v0',
    entry_point='gym_ai_lab.envs:LavaFloorEnv')
register(
    id='VeryBadLavaFloor-v0',
    entry_point='gym_ai_lab.envs:VeryBadLavaFloorEnv')
register(
    id='NiceLavaFloor-v0',
    entry_point='gym_ai_lab.envs:NiceLavaFloorEnv')
register(
    id='BiggerLavaFloor-v0',
    entry_point='gym_ai_lab.envs:BiggerLavaFloorEnv')
register(
    id='HugeLavaFloor-v0',
    entry_point='gym_ai_lab.envs:HugeLavaFloorEnv')
register(
    id='LavaFloorExam2018-v0',
    entry_point='gym_ai_lab.envs:LavaFloorExam2018Env')

register(
    id='CliffWalkingExam2018-v0',
    entry_point='gym_ai_lab.envs:CliffWalkingExam2018Env')
