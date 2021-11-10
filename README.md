# dockerp1mqtt

sudo apt install gnupg2 pass
docker image build -t dockerp1mqtt:latest  .
docker login -u revenberg
docker image push revenberg/dockerp1mqtt:latest

docker run revenberg/dockerp1mqtt

docker exec -it ??? /bin/sh

docker push revenberg/dockerp1mqtt:latest