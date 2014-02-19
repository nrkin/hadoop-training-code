#!/usr/bin/python
import sys
from datetime import datetime
import re

N_ADDED_AT = 8
N_STUDENT_ID = 3
TZ_LEN = 3
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

def ignore_tz(t):
    return t[:-TZ_LEN]

def get_hour(d):
    d = ignore_tz(d)
    try:
        dt = datetime.strptime(d, DATETIME_FORMAT)
        return dt.hour
    except ValueError:
        return None

def remove_quotes(word):
    return re.sub("\"", "", word)

for line in sys.stdin:
    words = line.strip().split("\t")
    if len(words) >= N_ADDED_AT:
        student_id = remove_quotes(words[N_STUDENT_ID])
        added_at_hr = remove_quotes(words[N_ADDED_AT])
        added_at_hr = get_hour(added_at_hr)
        if added_at_hr:
            print "{0}\t{1}".format(student_id, added_at_hr)
