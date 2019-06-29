#!/bin/bash


# This script generates the input for netcat
# Run it like so: ./script25.txt > dict.txt
# Then use the generated input: nc localhost 30002 < dict.txt
# Tip, if you are getting timeout try removing the first 5000 lines of dict.txt


pass24=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

pin=0

while [ $pin -lt 10000 ]; do

    echo -e $pass24 $pin

    ((pin++))

done

