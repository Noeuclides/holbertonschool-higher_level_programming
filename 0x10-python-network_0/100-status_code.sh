#!/bin/bash
# display only the status code of the response.
curl -sw %{http_code} $1 -o /dev/null
