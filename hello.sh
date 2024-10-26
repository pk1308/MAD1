#!/bin/bash
while true; do
    { echo -e "Today's date and time is \n\t $(date)"; } | nc -l -p 3500
done
