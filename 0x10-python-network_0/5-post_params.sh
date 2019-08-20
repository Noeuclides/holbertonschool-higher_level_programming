#!/bin/bash
# send POST request, and display body response
curl -sX POST $1 -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD'
