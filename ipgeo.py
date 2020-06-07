#!/usr/bin/python

import sys
import socket
import requests

if len(sys.argv) == 1:
    print("Please specify an IP address, or 'me' to look up your own current IP.\nUsage: ipgeo <ip address>")
    sys.exit()
else:
    ip = sys.argv[1]

# --- get your own IP address ---
if not ip or ip in [ 'self', 'mine', 'me', 'my', 'own', 'local', 'current']:
    r = requests.get('https://curlmyip.org')
    ip = r.text

# --- validate IP address ---
try:
    socket.inet_aton(ip)
except:
    print(f"Invalid IP address: {ip}")
    sys.exit()

# --- get the info ---
response = requests.get('http://ip-api.com/json/%s' % ip).json()

if response['status'] == 'fail':
    print("Lookup of IP \"%s\" failed!\nFail message from API: %s" % (ip, response['message']))
    sys.exit()

print("IP:      %s\nCity:    %s\nRegion:  %s\nCountry: %s" % (ip, response['city'], response['region'], response['country']))