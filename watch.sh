#!/bin/bash
dom() {
      python ~/Incubator/cumb.py
      scp users.db af_server@woop.ac:/home/af_server/game/config/users
      scp groups.db af_server@woop.ac:/home/af_server/game/config/groups
      scp users.db af_server@califa.actionfps.com:/home/af_server/game/config/users
      scp groups.db af_server@califa.actionfps.com:/home/af_server/game/config/groups
}
dom
inotifywait -m -e close_write,moved_to,create  . |
while read -r directory events filename; do
  if [ "$events" = "CLOSE_WRITE,CLOSE" ]; then
  	if [[ "$filename" == *.pub ]]; then
dom
    fi
fi
done
