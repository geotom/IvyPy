"""Query the IronVoice API."""

import urllib

class ivapi:
    
    def __init__(self, host = None, key = None):
        #if isinstance(host, basestring) and isinstance(key, basestring):
        if (host is None) and (key is None):
            try:
                import ironvoiceapi_conf
                host, key = ironvoiceapi_conf.host, ironvoiceapi_conf.key
            except:
                raise Exception('Configuration file "ironvoiceapi_conf.py" not found.')
        try:
            self.base_url = '{}/api/?key={}&'.format(host, key)
            url_test = urllib.urlopen('{}method=get'.format(self.base_url))
            okay = next(url_test)
        except:
            raise Exception('Invalid host and/or API key.')
    
    def trace(self, host):
        hops = []
        return hops

    def peers(self):
        peers_dict = {}
        print next(urllib.urlopen('{}method=peers'.format(self.base_url)))
        return peers_dict

    
