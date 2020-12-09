#!/bin/sh

echo "foo" > ${OUTPUT}/test.txt

while true; do
  echo "Starting export of teamvault"
  /app/teamvaultexport.py -a ${AUTH} -u ${URL} -o ${OUTPUT}/$(date +"%Y%m%d%H%M%S").json
  sleep 86400
done

