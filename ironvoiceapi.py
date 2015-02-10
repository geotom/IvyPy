"""Query the IronVoice API."""

import urllib
import json

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
            self.base_url = '{}/api/?key={}'.format(host, key)
            url_test = urllib.urlopen('{}&method=get'.format(self.base_url))
            okay = next(url_test)
        except:
            raise Exception('Invalid host and/or API key.')

    def make_query(self, method, params = None):
        query_url = '{}&method={}'.format(self.base_url, method)
        if params and len(params) > 0:
            for key, value in params:
                query_url = '{}&{}={}'.format(query_url, key, value)
        reply = next(urllib.urlopen(query_url), None)
        if reply:
            try:
                return json.loads(reply)
            except:
                return reply
        else:
            return None

    def trace(self, host):
        return self.make_query(
                    method = 'trace',
                    params = (
                        ('host', str(host)),
                    )
        )

    def peers(self):
        return self.make_query(method = 'peers')

