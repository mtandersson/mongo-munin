
import urllib2
import sys
import os

try:
    import json
except ImportError:
    import simplejson as json


def getServerStatus():
    host = os.environ.get("host", "127.0.0.1")
    port = os.environ.get("port", "28017")
    url = "http://%s:%s/_status" % (host, port)
    req = urllib2.Request(url)
    user = os.environ.get("user")
    password = os.environ.get("password")
    if user and password:
        passwdmngr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passwdmngr.add_password(None, 'http://%s:%d' % (host, port), user, password)
        authhandler = urllib2.HTTPDigestAuthHandler(passwdmngr)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
    raw = urllib2.urlopen(req).read()
    return json.loads( raw )["serverStatus"]
