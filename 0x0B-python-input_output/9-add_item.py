#!/usr/bin/python3
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


my_list = []
filename = 'add_item.json'
if os.path.isfile(filename):
    if os.stat(filename).st_size > 0:
        my_list = load_from_json_file(filename)
my_list += [arg for arg in sys.argv[1:]]
save_to_json_file(my_list, filename)
