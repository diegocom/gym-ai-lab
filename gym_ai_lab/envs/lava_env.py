from gym_ai_lab.envs.obsgrid_env import ObsGrid


class LavaFloorEnv(ObsGrid):
    """
    The floor is lava! Actions have a stochastic outcome
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["F", "F", "F", "G"],
                ["F", "W", "F", "P"],
                ["S", "F", "F", "F"]
            ]
        rewards = {"F": -0.04, "S": -0.04, "P": -1.0, "G": 1.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)


class VeryBadLavaFloorEnv(ObsGrid):
    """
    The floor is lava! Actions have a stochastic outcome
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["F", "F", "F", "G"],
                ["F", "W", "F", "P"],
                ["S", "F", "F", "F"]
            ]
        rewards = {"F": -5, "S": -5, "P": -1.0, "G": 1.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)


class NiceLavaFloorEnv(ObsGrid):
    """
    The floor is lava! Actions have a stochastic outcome
    """
    def __init__(self):
        actions = {0: "L", 1: "R", 2: "U", 3: "D"}
        grid = [
                ["F", "F", "F", "G"],
                ["F", "W", "F", "P"],
                ["S", "F", "F", "F"]
            ]
        rewards = {"F": 5, "S": 5, "P": -1.0, "G": 1.0}
        actdyn = {0: {0: 0.8, 1: 0.0, 2: 0.1, 3: 0.1}, 1: {1: 0.8, 0: 0.0, 2: 0.1, 3: 0.1}, 2: {2: 0.8, 1: 0.1, 0: 0.1,
                  3: 0.0}, 3: {3: 0.8, 1: 0.1, 2: 0.0, 0: 0.1}}
        super().__init__(actions, grid, actdyn, rewards)
