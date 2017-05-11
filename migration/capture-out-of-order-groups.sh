#!/bin/bash
# List the first message of a group that is backwards in time.
# Provide the last valid message and the first broken one.
mawk -v OFS=$'\t' -F $'\t' '{ if ( $1 < last_time)  { if ( !done ) { print prev_message; print; print ""; done = 1} } else { last_time = $1; prev_message = $0; done = 0 } }'
