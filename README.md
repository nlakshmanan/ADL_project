# Surreal with Pybullet-Gym

## Problem Statement

Deep RL is facing a high barrier in terms of compute infrastructure, reproducibility, and implementing data-hungry algorithms  rapidly to try new ideas. This has given rise to a need for an open-source scalable framework that supports distributed reinforcement learning algorithms. One such framework is SURREAL, developed by Stanford Vision and Learning Lab (SVL).

SURREAL provides flexibility to choose environment and supports two environment suites:<br />
(1) [Robosuite](https://github.com/StanfordVL/robosuite) <br />
(2) [OpenAI Gym MuJoCo](https://gym.openai.com/envs/#mujoco)

Both these environment suites use [MuJoCo](http://www.mujoco.org/) as its physics engine which requires a paid licence. This project incorporates a new environment suite [pybullet-gym](https://github.com/benelot/pybullet-gym) which is an open source implementation of OpenAI Gym MuJoCo environment. 

### Input and Output
Input is an command with environment and algorithm. <br/>
Example: surreal_subproc.py -al ppo --env gym:HalfCheetahPyBulletEnv-v0 exp1 <br/>
Here the algorithm is Surreal's inbuilt PPO algorithm and environment is pybullet-gym's half-cheetah.<br/>

Output is tensorboard running at http://localhost:6006/  that shows training status.

## Deliverables:
(1)Run SURREAL without MuJoCo by providing SURREAL with pybullet-gym support <br />
(2)Docker image <br />
(3)Docker File

## Surreal CLI with PyBullet-Gym environments

surreal_subproc.py [-h] [-al ALGORITHM] [-na NUM_AGENTS][-ne NUM_EVALS] [--env ENV]  [-dr] Experiment_name <br/>

-al : Algorithm - ddpg / ppo or the location of algorithm python script <br/>
-na : number of agent pods to run in parallel.<br/>
-ne : number of eval pods (rewards evaluators) to run in parallel.<br/>
--env : Environment, the [supported environments](https://github.com/benelot/pybullet-gym#state-of-implementations) have a prefix of "gym:". Example: gym:HalfCheetahPyBulletEnv-v0. <br/>
-dr: Dry run print the subprocess commands without actually running. <br/>
Experiment_name: experiment name under which checkpoint will be saved


## Run Surreal with PyBullet-Gym

### Option1: Run from code
Step 1: Git clone the repository
```
git clone https://github.com/nlakshmanan/ADL_project.git
``` 
Step 2: Create a virtual environment
```
mkdir venv
cd venv
python3 -m venv .
source ./bin/activate
```
Step 3: Go to the local cloned directory 
```
cd /Users/Admin/Desktop/ADL_project
```

Step 4: Install requirements and execute Setup Files
```
cd ./surreal
pip install -r requirements.txt
python3 setup.py install
cd ../pybullet-gym
pip install -e .
```
Step 5: Install pytorch
```
pip install torch torchvision
```
Step 6: Create YML File
```
surreal-default-config
```
Step 7: Edit 'username' and 'subproc_results_folder' in YML File
```
vi ~/.surreal.yml
```
Step 8: Launch training
```
cd ADL_project/surreal/surreal/subproc
python3 surreal_subproc.py -al ppo --env gym:HalfCheetahPyBulletEnv-v0 exp1
```

### Option2: Run from docker
Step 1: Pull image from docker
```
docker pull nnlnachu/surreal_pybullet:latest
```
Step 2: Run the docker image
```
docker run -it surreal-pybullet bash
```
Step 3: Install dependencies
```
cd ./surreal
python3 -m pip install -r requirements.txt
python3 -m pip install torch
python3 -m pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.1.0-cp37-cp37m-manylinux2010_x86_64.whl
python3 setup.py install
cd ../pybullet-gym
python3 setup.py install 
```
Step 4: Launch training
```
cd ../surreal/surreal/subproc
python3 surreal_subproc.py -al ppo --env gym:HalfCheetahPyBulletEnv-v0 exp1
```

## Building Image from Docker File
Prequisites: [Install docker](https://docs.docker.com/install/) 

Step 1: Git clone the repository
```
git clone https://github.com/nlakshmanan/ADL_project.git
``` 
Step 2:  Go to the local cloned directory 
```
cd /Users/Admin/Desktop/ADL_project
```
Step 3: Build docker image
This commands take a long time to complete. Please wait until it completes.
```
docker build -t surreal-pybullet .
```
Step 4: Run docker image 
```
docker run -it surreal-pybullet bash
```

