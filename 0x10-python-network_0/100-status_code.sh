#!/bin/bash
# send POST request, and display body response
curl -sI POST $1 | head -1 | cut -d" " -f2
