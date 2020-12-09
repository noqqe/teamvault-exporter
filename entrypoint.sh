#!/bin/sh

echo "foo" > ${OUTPUT}/test.txt

while true; do
  echo "Starting export of teamvault"
  STAMP=$(date +"%Y%m%d%H%M%S")
  /app/teamvaultexport.py -a ${AUTH} -u ${URL} -o ${OUTPUT}/$STAMP.json
  echo $PASSPHRASE | gpg --batch --passphrase-fd 0 -c ${OUTPUT}/$STAMP.json &&  rm ${OUTPUT}/$STAMP.json
  # Decrypt
  # echo $PASSPHRASE | gpg --batch --passphrase-fd 0 -d ${OUTPUT}/$STAMP.json.gpg
  sleep 86400
done

