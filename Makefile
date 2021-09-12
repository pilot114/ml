start:
	docker run -p 8888:8888 -v ${PWD}:/tf/my -w /tf/my --name ml tensorflow/tensorflow:latest-jupyter &
stop:
	docker stop ml && docker rm ml