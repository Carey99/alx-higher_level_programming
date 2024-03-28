#!/bin/bash
#Displays all HTTP methods
curl -sI "$1" | grep -i allow
