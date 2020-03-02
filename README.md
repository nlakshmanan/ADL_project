# ADL_project
Surreal with Pybullet-Gym

# Steps to create docker image
Prequisites: Have docker installed in you system where you want to create a docker image of this repository.

## Git clone the repository
```
git clone https://github.com/nlakshmanan/ADL_project.git
```


## Go to the directory where you cloned
```
cd /Users/Admin/Desktop/ADL_project
```

## Build docker image
This commands take a long time to complete. Please wait until it completes.
```
docker build -t surreal-Pybullet .
```

## Run docker image 
```
docker run -it surreal-Pybullet bash
```
