FROM tensorflow/tensorflow

RUN apt-get update -qq && \
    apt-get install --no-install-recommends -y \
    git \
    python3-opengl \
    zlib1g-dev \
    libjpeg-dev \
    patchelf \
    cmake \
    swig \
    libboost-all-dev \
    libsdl2-dev \
    libosmesa6-dev \
    xvfb \
    ffmpeg \
    fceux

RUN pip --no-cache-dir install \
    keras \
    gym \
    git+https://github.com/joshuansu0897/gym-super-mario 

WORKDIR /app

COPY . .

CMD [ "python", "Mario.py" ]
