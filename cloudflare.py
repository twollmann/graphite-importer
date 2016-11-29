#!/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import urllib2
import socket
import yaml
import json

class cloudflare:

    def __init__(self):
        for zone in config['cloudflare']:
            self.get_metrics(zone['email'], zone['key'], zone['url'])
            self.extract_metrics(zone['name'])
            self.send_graphite()

    def get_metrics(self, email, key, url):
        self.req = urllib2.Request(url)
        self.req.add_header('Content-Type', 'application/json')
        self.req.add_header('X-Auth-Key', key)
        self.req.add_header('X-Auth-Email', email)
        self.c = urllib2.urlopen(self.req)
        self.data = self.c.read()
        self.c.close()

    def extract_metrics(self, name):
        self.message = ''
        self.metrics = json.loads(self.data)
        for series in self.metrics['result']['timeseries']:
            timestamp = int(datetime.strptime(series['until'], '%Y-%m-%dT%H:%M:%SZ').strftime("%s"))
            for section in ['requests', 'bandwidth', 'threats']:
                for key, val in series[section].iteritems():
                    if isinstance(val, dict):
                        for subkey, subval in val.iteritems():
                            self.message += "cloudflare.{}.{}.{}.{} {} {}\n".format(name, section, key, subkey, subval, timestamp)
                    else:
                        self.message += "cloudflare.{}.{}.{} {} {}\n".format(name, section, key, val, timestamp)

    def send_graphite(self):
        self.sock = socket.socket()
        self.sock.connect((config['carbon']['server'], config['carbon']['port']))
        self.sock.sendall(self.message)
        self.sock.close()

if __name__ == "__main__":
    global config
    with open("config.yml", 'r') as ymlfile:
        config = yaml.load(ymlfile)
    cloudflare()
