from __future__ import print_function
import string
import sys
import json
import urllib2


CACHE_FILE = 'macs.cache'
LOOKUP_URL = "http://api.macvendors.com/%s"
CACHE = {}


def identify(macaddr):
    macaddr = ''.join([c for c in macaddr if c in string.hexdigits]).lower()
    if len(macaddr) != 12:
        raise ValueError("%s is not a valid mac address" % macaddr)

        if macaddr in CACHE:
            return CACHE[macaddr]
        try:
            with urllib2.urlopen(LOOKUP_URL%macaddr) as u:
                desc = u.readline()
        except urllib2.HTTPError as e:
            if e.code == 404:
                return ''
            raise
        f.write(' '.join([macaddr, desc]))

def init_cache():
    global CACHE
    try:
        with open(CACHE_FILE, 'a+') as f:
            CACHE = json.load(f)
    except ValueError:
        CACHE = {}

def save_cache():
    with open(CACHE_FILE, 'w') as f:
        json.dump(CACHE, f) 