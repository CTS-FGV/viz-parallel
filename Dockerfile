FROM python:3.6

# Set the working directory to /app
WORKDIR /app

RUN pip install dash==0.19.0
RUN pip install dash-renderer==0.11.1
RUN pip install dash-html-components==0.8.0
RUN pip install dash-core-components==0.14.0
RUN pip install plotly
RUN pip install gunicorn
RUN pip install pandas

# Expose a port 
EXPOSE  5000

# Run app.py when the container launches
CMD gunicorn -w 2 -b 0.0.0.0:5000 -t 100000 --max-requests 20 --reload app:server