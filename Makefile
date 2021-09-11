start:
        @docker run -it -p 8888:8888 -v $PWD:/tf/my -w /tf/my tensorflow/tensorflow:latest-jupyter