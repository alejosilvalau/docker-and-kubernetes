# Define the image on which to build
FROM python:3.10

# Copy files/folders to the main folder of the container
COPY . . 

# Install the application's dependencies
RUN pip install -r requirements.txt

# Run the script when the container starts
ENTRYPOINT ["python", "hello_world.py"]