#!/bin/bash
# display all HTTP methods the server will accept.
curl -sI $1 | head -4 | tail -1 | cut -d":" -f2 | sed 's/ //'
