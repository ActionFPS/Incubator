#!/bin/bash
dom() {
      python ~/Incubator/cumb.py
      scp users.db assaultcube@woop.ac:/home/assaultcube/latest/ag/config/users
      scp groups.db assaultcube@woop.ac:/home/assaultcube/latest/ag/config/groups

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
