import h5py
import json

# read the hdf5 file
file_path = "/home/pouyan/phd/imitation_learning/robomimic/datasets/can/ph/my_test.hdf5"
with h5py.File(file_path, "r") as f:
    print("==== Env data ====")
    # print(list(f.keys()))  # ['data', 'mask']
    # print(f['mask'])  # <HDF5 group "/mask" (8 members)>
    # print(f['data'])  # <HDF5 group "/data" (200 members)>
    print(f['data'].attrs['total'])  # total number of state-action pairs
    print(f['data']['demo_0'].keys())  # <KeysViewHDF5 ['actions', 'dones', 'next_obs', 'obs', 'rewards', 'states']>
    print(f['data']['demo_0']['obs'].keys())  # <KeysViewHDF5 ['object', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_eef_quat_site', 'robot0_gripper_qpos', 'robot0_gripper_qvel', 'robot0_joint_pos', 'robot0_joint_pos_cos', 'robot0_joint_pos_sin', 'robot0_joint_vel']>
    # print(f['data']['demo_0']['rewards'].shape)
    #print(f['mask'].keys()) # <KeysViewHDF5 ['20_percent', '20_percent_train', '20_percent_valid', '50_percent', '50_percent_train', '50_percent_valid', 'train', 'valid']>

    print("==== Env Meta ====")
    env_meta = json.loads(f["data"].attrs["env_args"])
    print(json.dumps(env_meta, indent=4))
    print("")
    print("==== robot ====")
    print(env_meta["env_kwargs"]["robots"])

# edit the hdf5 file
# with h5py.File(file_path, "a") as f:
#     env_meta["env_kwargs"]["robots"] = ["Sawyer"]
#     f["data"].attrs["env_args"] = json.dumps(env_meta)
#     print("Updated robot value:", env_meta["env_kwargs"]["robots"])


