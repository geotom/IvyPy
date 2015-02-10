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
            self.base_url = '{}/api/?key={}'.format(host, key)
            url_test = urllib.urlopen('{}&method=get'.format(self.base_url))
            okay = next(url_test)
        except:
            raise Exception('Invalid host and/or API key.')

    def _make_query(self, method, params = None):
        query_url = '{}&method={}'.format(self.base_url, method)
        if isinstance(params, dict):
            for param in params.items():
                if param[1]:
                    query_url = '{}&{}={}'.format(query_url, param)
                else:
                    query_url = '{}&{}'.format(query_url, param[0])
        return urllib.urlopen(query_url)

    def trace(self, host):
        result = self._make_query(
                method = 'trace',
                params = {'host': str(host)},
        )
        hops = []
        return hops

    def peers(self):
        results = self._make_query(method = 'peers')
        for result in results:
            print result

    
