#!/usr/bin/python

import sys
import csv

TAG = 2
ID = 0
TYPE = 5

reader = csv.reader(sys.stdin, delimiter='\t')
for parts in reader:
    if len(parts) <= TYPE:
        continue

    post_id = parts[ID]
    tags_list = parts[TAG]
    node_type = parts[TYPE]

    if node_type != "question" or tags_list == "":
        continue

    tags = tags_list.split(" ")
    for tag in tags:
        print "{0}\t{1}".format(tag, post_id)

