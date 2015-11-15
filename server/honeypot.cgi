#!/usr/bin/env python2
from __future__ import print_function

import cgi
import json

print("Content-Type: text/html\n\n")  # html markup follows

SETTINGS_FILE = "config.json"
DEFAULT_SETTINGS = {"recents":[], "global":{}, "known":[]}
OPTIONS = "recents".split()
LASTSEENFIELDS = ["Known?", "MAC Address", "Last seen"]
GLOBALFIELDS = ["Name", "Phone", "Email"]
for f in GLOBALFIELDS:
    DEFAULT_SETTINGS['global'][f] = ''
DEFAULT = "<i>???</i>"

try:
    with open(SETTINGS_FILE) as f:
        settings = json.load(f)
except (IOError, ValueError):
    settings = DEFAULT_SETTINGS


with open('start.html') as f:
    htmlFormat1 = f.read()

def formatrow(row, startcol='<td>', endcol='</td>'):
    return "<tr>"+"".join(startcol + entry + endcol for entry in row)+"</tr>"

table = [
    '<table style="width:100%">',
    formatrow(LASTSEENFIELDS, startcol='<th>', endcol='</th>')
]

with open(SETTINGS_FILE, 'r') as f:
    for i, user in enumerate(settings['recents']):
        if not isinstance(user, dict):
            del settings['recents'][i]
        entries = [user.get(field, DEFAULT) for field in LASTSEENFIELDS]
        table.append(formatrow(entries))

table.append("</table>")

htmlFormat2 = """
                </div>
            </div>
        </div>
    </body>
</html> """

form = cgi.FieldStorage()



with open(SETTINGS_FILE, "w") as f:
    for field in GLOBALFIELDS:
        settings['global'][field] = form.getfirst(field, settings.get(field, ''))
    json.dump(settings, f, separators=(',', ': '), indent=2)

print(htmlFormat1 + '\n'.join(table) + htmlFormat2) # see embedded %s ^ above
