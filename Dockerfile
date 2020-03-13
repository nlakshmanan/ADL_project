# getting base image python:3
FROM python:3.7

MAINTAINER <nachammailakshmanan2019@u.northwestern.edu>


COPY ./surreal /code/surreal
COPY ./pybullet-gym /code/pybullet-gym

WORKDIR /code

COPY ./surreal/surreal/sample_surreal.yml  /root/.surreal.yml



