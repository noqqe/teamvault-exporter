#!/bin/sh

echo "Starting export of teamvault"
/app/teamvaultexport.py -a ${AUTH} -u ${URL} -o ${OUTPUT}/$(date +"%Y%m%d%H%M%S").json

