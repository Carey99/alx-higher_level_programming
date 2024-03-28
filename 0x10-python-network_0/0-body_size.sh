#!/bin/bash
#Display request in bytes
curl -s -w "%{size_download}\n" -o /dev/null "$1"
