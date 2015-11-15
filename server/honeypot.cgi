#!/usr/bin/env python2

import cgi
import json


print("Content-Type: text/html\n\n")  # html markup follows


htmlFormat = """
<html>
	<head>
		<title>HoneyPot</title>
		<style>
			body {
			font-family: "Trebuchet MS";
			vertical-align: middle;
			font-size: 100%;
			width: 1280px;
			height: 100%;
			padding: 3px;
			margin: 0px;
			margin-left: auto;
			margin-right: auto;
			}
			#status {
			white-space: pre;
			text-overflow: ellipsis;
			overflow: hidden;
			max-width: 400px;
			}
			#mainContent{
			background-color:#EEEEEE;
			border-radius: 5px;
			padding: 10px;
			}
			#headerbar{
			position: float;
			background-color: #D7A015;
			height: 40px;
			width: 100%;
			vertical-align: middle;
			text-align: center;
			color: #FFFFFF;
			font-size: 30px;
			margin-top:auto;
			margin-bottom:6px;
			border-radius: 5px;
			}
			#headerbar span{
			margin-top:auto;
			margin-bottom:auto;
			vertical-align: middle;
			}
		</style>
		<style type="text/css">
		    .container {
		        width: 600px;
		        clear: both;
		    }
		    .container input {
		        width: 100%;
		        clear: both;
		    }
		</style>
		<style>
			.boxed {
			    border: 1px solid gray;
			    padding: 10px;
			}
		</style>
		<style>
			table, th, td {
			    border: 1px solid black;
			    border-collapse: collapse;
			}
			th, td {
			    padding: 5px;
			}
		</style>
	<!-- <script src="popup.js"></script> -->
	</head>
	<body>
		<div id="headerbar"><span>HoneyPot</span></div>
		<div style="height:30px; "></div>
			<div class="container", style="width:100%">
				<div class="boxed", style="float:left; width:47%">
					<center>
						<div style="color:#000000">
							<h3>Welcome to HoneyPot</h3>
							<p>Here, you can change the settings on your device to match your needs.</p>
						</div>
					</center>
					<div style="height:30px; "></div>
					<form action="http://localhost:8000" method="post">
						 <label>First Name</label>
						 <div style="height:10px; "></div>
						 <input type="text" name="first" style="font-size:14pt;height:35px;width:600px;"><br />
						 <div style="height:30px; "></div>
						 <label>Last Name</label>
						 <div style="height:10px; "></div>
						 <input type="text" name="last" style="font-size:14pt;height:35px;width:600px;"><br />
						 <div style="height:30px; "></div>
						 <label>Phone Number</label>
						 <div style="height:10px; "></div>
						 <input type="test" name="number" style="font-size:14pt;height:35px;width:600px;"><br />
						 <div style="height:30px; "></div>
						 <label>Email</label>
						 <div style="height:10px; "></div>
						 <input type="text" name="email" style="font-size:14pt;height:35px;width:600px;"><br />
						 <div style="height:20px; "></div>
						 <input type="submit" value="Submit">
					</form>
				</div>
				<div class="boxed", style="float:right; width:47%">
					<center>
						<div style="color:#000000">
							<h3>Devices Already Added</h3>
						</div>
					</center>
					<table style="width:100%">
						 <tr>
						    <th>Name</th>
						    <th>MAC Address</th> 
						    <th>Time Added</th>
						 </tr>
						 <tr>
						    <td>Emily Smith</td>
						    <td>1.234.56.7.8</td> 
						    <td>3:14:47</td>
						 </tr>
					</table>
				</div>
			</div>
		</div>
	</body>
</html> """

form = cgi.FieldStorage()

fields = "first last phone email".split()
SETTINGS_FILE = "config.json"

try:
    with open(SETTINGS_FILE) as f:
        current = json.load(f)
except IOError:
    current = {}

with open(SETTINGS_FILE, "w") as f:
    for field in fields:
        current[field] = form.getfirst(field, current.get(field, ''))
    json.dump(current, f)

print(htmlFormat) # see embedded %s ^ above
