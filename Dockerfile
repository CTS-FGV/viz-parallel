FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN pip install -r requirements.txt

# Expose a port 
EXPOSE  5000

# Run app.py when the container launches
CMD gunicorn -w 10 -b 0.0.0.0:5000 -t 100000 --max-requests 20 app:server

