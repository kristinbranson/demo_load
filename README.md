# Demo code for reading Branson Lab file formats

* Main script: demo_load_trajectories.py
* Sample data: demo_trajectory_data
* Requires APT to be downloaded somewhere.
* I used the transformer conda environment from
[AnimalPoseForecasting](https://github.com/kristinbranson/AnimalPoseForecasting/tree/kb_working/environment)
* You can also use the APT docker environment:
`docker pull bransonlabapt/apt_docker:apt_20230427_tf211_pytorch113_ampere`

Startup:
```
conda activate transformer
export PYTHONPATH="$HOME/tracking/code/APT/deepnet"
export MPLBACKEND=tkagg
python demo_load_trajectories.py
```
