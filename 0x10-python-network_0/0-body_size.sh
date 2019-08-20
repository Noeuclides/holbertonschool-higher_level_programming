#!/bin/bash
# send a request to a URL, and display the size of body response
curl -s $1 | wc -m
