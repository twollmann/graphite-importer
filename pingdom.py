#!/bin/env python
# -*- coding: utf-8 -*-

import socket
import urllib2
import base64
import json
import yaml

class pingdom:

    def __init__(self):
        self.config = self.load_config()
        self.message = self.get_metrics(self.config)
        self.send_graphite(self.message, self.config)

    def load_config(self):
        with open("config.yml", 'r') as self.ymlfile:
            self.cfg = yaml.load(self.ymlfile)

    def get_metrics(self, cfg):
        self.message = ""
        self.credentials = base64.b64encode("{}:{}".format(self.cfg['pingdom']['username'], self.cfg['pingdom']['password']))
        for self.check in self.cfg['pingdom_checks']:
            self.url = "https://api.pingdom.com/api/2.0/results/{}?limit={}".format(self.check['id'], self.check['limit'])
            self.request = urllib2.Request(self.url)
            self.request.add_header("Authorization", "Basic %s" % self.credentials)
            self.request.add_header("app-key", self.cfg['pingdom']['app_key'])
            self.response = urllib2.urlopen(self.request)
            self.results = json.loads(self.response.read())
            for self.result in self.results['results']:
                self.message = self.message + "{} {} {}\n".format(self.check['name'], self.result['responsetime'], self.result['time'])
        return self.message

    def send_graphite(self, message, cfg):
        self.sock = socket.socket()
        self.sock.connect((self.cfg['carbon']['server'], self.cfg['carbon']['port']))
        self.sock.sendall(message)
        self.sock.close()

if __name__ == "__main__":
    pingdom()
