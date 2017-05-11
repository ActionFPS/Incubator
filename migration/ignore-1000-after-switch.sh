#!/bin/bash
mawk -F $'\t' '
    !($2 == "aura.woop.ac:10000" && $1 >= "2017-05-03T06:51:33.293Z") {
        print
    }
'