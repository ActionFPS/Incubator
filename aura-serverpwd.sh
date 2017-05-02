#!/bin/bash
SOURCE_FILE=/home/assaultcube/config/serverpwd.cfg
REDACTED_FILE=/home/assaultcube/demos/logs/serverpwd_redacted.txt
dom() {
  cat ${SOURCE_FILE} |awk '{ if ( $0 !~ /^\/\// ) { print "// REDACTED LINE " } else print }' > ${REDACTED_FILE}
  scp ${SOURCE_FILE} califac@califa.actionfps.com:/home/califac/assaultcube/config/serverpwd.cfg
}
dom
inotifywait -m -e close_write,moved_to,create ${SOURCE_FILE} |
while read -r directory events filename; do
  if [ "$events" = "CLOSE_WRITE,CLOSE" ]; then
    dom
  fi
done

