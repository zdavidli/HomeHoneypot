from __future__ import print_function
import string
import sys


CACHE_FILE = 'macs.cache'
LOOKUP_URL = "http://api.macvendors.com/"


def identify(macaddr):
    macaddr = ''.join([c for c in macaddr if c in string.hexdigits]).lower()
    if len(macaddr) != 12:
        raise ValueError("%s is not a valid mac address" % macaddr)

    with open(CACHE_FILE, 'a+') as f:
        f.seek(0)
        for line in f.readlines():
            mac, desc = line.split(' ')
            if macaddr == mac.lower():
                return desc
        try:
            with urllib2.urlopen(LOOKUP_URL+macaddr) as u:
                desc = u.readline()
        except urllib2.HTTPError as e:
            if e.code == 404:
                return ''
            raise
        f.write(' '.join([macaddr, desc]))



