#!/bin/bash
#Displays all HTTP methods
curl -sI "$1" | grep "allow" | cut -d " " -f 2- 
