docker container stop skiptir
docker container rm skiptir
docker build . -t skiptir:example
docker run -d --name=skiptir -p 8080:8080 skiptir:example
