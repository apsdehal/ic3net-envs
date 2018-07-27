from gym.envs.registration import register

register(
    id='PredatorPrey-v0',
    entry_point='gccnet_envs.predator_prey_env:PredatorPreyEnv',
)

register(
    id='TrafficJunction-v0',
    entry_point='gccnet_envs.traffic_junction_env:TrafficJunctionEnv',
)
