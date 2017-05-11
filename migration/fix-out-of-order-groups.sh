#!/bin/bash
# overwrite each timestamp that is out-of-order with the latest timestamp we've seen so far.
# It's a hack really.
awk -v OFS=$'\t' -F $'\t' '{ if ( $1 < last_time )  { print last_time, $2, $3; } else { last_time = $1; prev_message = $0; print } }' 
