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

#
# Update settings
#

try:
    with open(SETTINGS_FILE) as f:
        settings = json.load(f)
except (IOError, ValueError):
    settings = DEFAULT_SETTINGS

changed = False
def default(f):
    global changed
    changed = True
    return settings.get(field, '')

form = cgi.FieldStorage()
for field in GLOBALFIELDS:
    settings['global'][field] = form.getfirst(field, default(field))

with open(SETTINGS_FILE, "w") as f:
    json.dump(settings, f, separators=(',', ': '), indent=2)

#
# Render page with new settings
#

with open('start.html') as f:
    html = f.read()
html %= settings['global']

def formatrow(row, startcol='<td>', endcol='</td>'):
    return "<tr>"+"".join(startcol + entry + endcol for entry in row)+"</tr>"
table = [
    '<table style="width:100%">',
    formatrow(LASTSEENFIELDS, startcol='<th>', endcol='</th>')
]
for i, user in enumerate(settings['recents']):
    if not isinstance(user, dict):
        del settings['recents'][i]
    entries = [user.get(field, DEFAULT) for field in LASTSEENFIELDS]
    table.append(formatrow(entries))
table.append("</table>")
html += '\n'.join(table) 
html += """
                </div>
            </div>
        </div>
    </body>
</html> """

print(html)
