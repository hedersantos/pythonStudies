#! /bin/bash

#scriptsPath=$(pwd)/pythonScripts

#echo scriptsPath

# remove container or evaluate error to true if it doesnt exist
docker rm pythonStudies || true

docker run -it -v $(pwd)"/pythonScripts":"/home/pythonScripts" --name pythonStudies python bash
