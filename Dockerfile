FROM jfloff/alpine-python:3.8-onbuild

# Install App
RUN mkdir /app
WORKDIR /app
COPY teamvaultexport.py /app/
RUN chmod +x /app/teamvaultexport.py

# Setup Cronjob
COPY periodic.sh /etc/periodic/15min/
RUN chmod +x /etc/periodic/15min/periodic.sh
CMD crond -f -l 5
