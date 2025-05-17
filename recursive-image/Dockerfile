FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3 git ca-certificates  # Install git and ca-certificates
RUN git clone https://github.com/alejosilvalau/docker-and-kubernetes.git /docker-and-kubernetes/
WORKDIR /docker-and-kubernetes/first-image/
RUN python hello_world.py