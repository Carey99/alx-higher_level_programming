#!/bin/bash
#Displays only body of a 200 status code
curl -s "$1"|(read code && [ "$code" == "200" ] && cat)
