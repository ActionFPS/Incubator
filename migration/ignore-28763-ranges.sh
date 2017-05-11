#!/bin/bash
mawk -F $'\t' '
    !(($1 <= "2016-07-03" && $2 == "62-210-131-155.rev.poneytelecom.eu aura AssaultCube[local#28763]")      || ($2 == "aura.woop.ac:28763" && $1 >= "2017-05-03") ) {
        print
    }
'