# getting base image python:3
FROM python:3.7

MAINTAINER <nachammailakshmanan2019@u.northwestern.edu>


COPY ./surreal /code/surreal
COPY ./pybullet-gym /code/pybullet-gym

WORKDIR /code

#RUN apt-get update
#RUN apt install python3-pip
#RUN apt-get build-dep python-pygame
#RUN apt-get install python-dev

#Install dependencies
#RUN apt-get install -y libsdl1.2-dev
COPY ./surreal/requirements.txt /code/
RUN pip install -r requirements.txt
RUN rm -r requirements.txt
RUN python3 -m pip install torch
RUN python3 -m pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.1.0-cp37-cp37m-manylinux2010_x86_64.whl

RUN python3 ./surreal/setup.py install 
#
RUN python3 ./pybullet-gym/setup.py install 
COPY ./surreal/surreal/sample_surreal.yml  /root/.surreal.yml

#Run a sample cmd
CMD ["python", "./surreal/subproc/surreal_subproc.py"]

