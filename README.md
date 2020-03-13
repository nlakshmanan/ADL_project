# Surreal with Pybullet-Gym

## Problem Statement

Deep RL is driven by data-hungry algorithms and a rising number of results are achieved by executing Deep RL algorithms in a distributed system. This has given rise to a need for an open-source scalable framework that supports distributed reinforcement learning algorithms. One such framework is SURREAL, developed by Stanford Vision and Learning Lab (SVL).

SURREAL provides flexibility to choose environment and in-built it supports two environment suites:

(1) [Robosuite](https://github.com/StanfordVL/robosuite)

(2) [OpenAI Gym MuJoCo](https://gym.openai.com/envs/#mujoco)

Both these environment suites use [MuJoCo](http://www.mujoco.org/) at backend as physics engine which requires a paid licence. This project incorporates a new environment suite [pybullet-gym](https://github.com/benelot/pybullet-gym) which is an open source implementation of OpenAI Gym MuJoCo environment. 

### Input and Output
Input is RL algorithm and environment that the user wants to train on.
Output is tensorboard that shows the training in progress.

## Deliverables:
(1)Run SURREAL without MuJoCo, embed SURREAL with an alternative simulator
(2)Docker image 
(3)Docker File

## Launch an Experiment

### Option1: Run from code (preffered)

### Option2: Run from docker

## Building Image from Docker File
Prequisites: [Install docker](https://docs.docker.com/install/) 

Step 1: Git clone the repository
```
git clone https://github.com/nlakshmanan/ADL_project.git
```


Step 2:  Go to the directory where you cloned
```
cd /Users/Admin/Desktop/ADL_project
```

Step 3: Build docker image
This commands take a long time to complete. Please wait until it completes.
```
docker build -t surreal-Pybullet .
```

Step 4: Run docker image 
```
docker run -it surreal-Pybullet bash
```
