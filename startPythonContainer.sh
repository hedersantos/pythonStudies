#! /bin/bash

# stop container if it's already running
docker stop pythonStudies || true

# start container in interactive mode
docker start -i pythonStudies

