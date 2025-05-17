## Installls the ubuntu image
FROM ubuntu

# Update the package manager
RUN apt-get update

# Install Python and Git
RUN apt-get install -y python3 git ca-certificates

# Clones this repository
RUN git clone https://github.com/alejosilvalau/docker-and-kubernetes.git /docker-and-kubernetes/

# Sets the working directory
WORKDIR /docker-and-kubernetes/first-image/

# Runs the hello_world.py script
RUN python hello_world.py