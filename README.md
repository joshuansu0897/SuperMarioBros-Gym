# SuperMarioBros GYM
Es un ejemplo de [```gym```](https://github.com/openai/gym) con **SuperMarioBros**

## Local
### Dependencies 

* keras (http://www.pyimagesearch.com/2016/11/14/installing-keras-with-tensorflow-backend/)
* tensorflow (https://www.tensorflow.org/install/)
* gym (https://github.com/openai/gym)
* gym-super-mario (https://github.com/joshuansu0897/gym-super-mario)

Use [pip](https://pip.pypa.io/en/stable/) to install any dependencies. 

## Docker
### Dependencies

* Docker (https://www.docker.com/)

Build
```
docker build . -t open-ia-mario
```

Run
```
docker run -it --user $(id -u) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --privileged open-ia-mario python Mario.py
```
