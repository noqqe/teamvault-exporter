FROM jfloff/alpine-python:3.8-onbuild

RUN apk add --update gnupg

# Install App
RUN mkdir /app
WORKDIR /app
COPY teamvaultexport.py /app/
RUN chmod +x /app/teamvaultexport.py

# Create Backup folder
RUN mkdir -p /var/backups/teamvault/

# Run Entrypoint
COPY entrypoint.sh /entrypoint.sh
CMD ["/entrypoint.sh"]
