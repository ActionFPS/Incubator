#~/bin/bash
mawk -F $'\t' -v OFS=$'\t' '{print substr($1,1,10),$2}'|mawk -F $'\t' -v OFS=$'\t' '$1 == last_date { counts[$2]++; } $1 != last_date { for ( i in counts ) print last_date, counts[i], i; last_date = $1;  delete counts; }; END {for ( i in counts ) print last_date, counts[i], i;}'
