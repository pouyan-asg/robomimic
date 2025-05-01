import h5py
import json

# read the hdf5 file
file_path = "/home/pouyan/phd/imitation_learning/robomimic/datasets/can/ph/my_test.hdf5"
with h5py.File(file_path, "r") as f:
    # print(list(f.keys()))  # ['data', 'mask']
    env_meta = json.loads(f["data"].attrs["env_args"])
    print("==== Env Meta ====")
    print(json.dumps(env_meta, indent=4))
    print("")
    print("==== robot ====")
    print(env_meta["env_kwargs"]["robots"])

# edit the hdf5 file
# with h5py.File(file_path, "a") as f:
#     env_meta["env_kwargs"]["robots"] = ["Sawyer"]
#     f["data"].attrs["env_args"] = json.dumps(env_meta)
#     print("Updated robot value:", env_meta["env_kwargs"]["robots"])


