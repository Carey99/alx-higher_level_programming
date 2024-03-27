#!/usr/bin/env bash
#Takes URL, send request & display

response=$(curl -s -w "%{size_download}" -o /dev/null "$1")

echo "$response"
