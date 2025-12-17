import h5py
import numpy as np
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset",
        type=str,
        default='/home/pouyan/phd/imitation_learning/robomimic/datasets/can/mh/low_dim_v15.hdf5',
        help="path to hdf5 dataset",
    )

    args = parser.parse_args()

    with h5py.File(args.dataset, 'r') as f:
        print(f.keys())
        print(f['data'].keys())
        print(f['mask'].keys())
        print(f['data']['demo_0'].keys())
        # print(f['data']['demo_0']['actions'].shape)
        # print(f['data']['demo_0']['dones'].shape)
        # print(f['data']['demo_0']['next_obs']['object'])
        # print(f['data']['demo_0']['obs'].shape)
        # print(f['data']['demo_0']['rewards'].shape)
        # print(f['data']['demo_0']['states'].shape)
        # action = f['actions']
        # state = f['states']
        # print(f"state shape: {state.shape}, action shape: {action.shape}")
        # print(f"minimum and maximum values:")
        # print(f"action: {np.min(action), np.max(action)}")
        # print(f"state: {np.min(state), np.max(state)}")
        # np.savetxt('output.txt', state[-1, :7], fmt='%.8f')
        # np.savetxt('all_states.txt', state, fmt='%.8f')
        # sample_s = state[0]
        # print(type(sample_s))
        # print(sample_s.shape)
        # print(sample_s)
        # print(np.min(action_np, axis=0), np.max(action_np, axis=0))
        # print(np.min(state), np.max(state))
        # print(np.min(state, axis=0), np.max(state, axis=0))


        # print(np.array(state))
        # for i in range(10):
        #     print(action[i])
        # print(action[50])