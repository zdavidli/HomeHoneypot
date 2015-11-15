from pushbullet import Pushbullet

api_key = "rgSZnZvSJi7EaOwQ4PKs4kdYJ4A3sNox"
pb = Pushbullet(api_key)
nexus5 = pb.devices[0]

def note(interface, device, mac_addr, notes):
    nexus5.push_note("HomeHoneypot: {1} detected on {0}".format(interface, device), "MAC address: {0}\n{1}".format(mac_addr, notes))