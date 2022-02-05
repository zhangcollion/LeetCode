import argparse
import numpy as np
import pandas as pd
import torch
from runner import Runner
from smac.env import StarCraft2Env
from common.arguments import get_common_args,  get_mixer_args

if __name__ == "__main__":
    ## get paras setting
    args = get_common_args()
    # get qmix paras
    if args.alg == "qmix":
        args = get_mixer_args(args)

    ## main part
    # create env
    env = StarCraft2Env(map_name=args.map,
                        step_mul=args.step_mul,
                        difficulty=args.difficulty,
                        game_version=args.game_version,
                        replay_dir=args.replay_dir)

    env_info = env.get_env_info()
    args.n_actions = env_info["n_actions"]
    args.n_agents = env_info["n_agents"]
    args.state_shape = env_info["state_shape"]
    args.obs_shape = env_info["obs_shape"]
    args.episode_limit = env_info["episode_limit"]
    runner = Runner(env, args)
    if not args.evaluate:
        runner.run(1)







    ## model train