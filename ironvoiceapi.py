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

    def make_query(self, method, **kwargs):
        query_url = '{}&method={}'.format(self.base_url, method)
        for key, value in kwargs.items():
            query_url = '{}&{}={}'.format(query_url, key, value)
        reply = next(urllib.urlopen(query_url), None)
        try:
            return json.loads(reply)
        except:
            return reply

    def trace(self, host):
        return self.make_query(
                method = 'trace',
                host = str(host),
        )

    def peers(self):
        return self.make_query(
                method = 'peers',
        )

    def recording(self, uid):
        return self.make_query(
                method = 'recording',
                uid = str(uid),
        )

    def recordings(self, extension):
        return self.make_query(
                method = 'recordings',
                extension = str(extension),
        )

    def call(self, dnid, extension, cid):
        return self.make_query(
                method = 'call',
                dnid = str(dnid),
                extension = str(extension),
                cid = str(cid),
        )

    def fax(self):
        return self.make_query(
                method = 'fax',
        )

    def inbox(self, mailbox):
        return self.make_query(
                method = 'inbox',
                mailbox = str(mailbox),
        )

    def voicemail(self, mailbox):
        return self.make_query(
                method = 'voicemail',
                mailbox = str(mailbox),
        )

    def archive(self, mailbox, message):
        return self.make_query(
                method = 'archive',
                mailbox = str(mailbox),
                message = str(message),
        )

    def cleanup(self, mailbox):
        return self.make_query(
                method = 'cleanup',
                mailbox = str(mailbox),
        )
    
    def purge(self, mailbox):
        return self.make_query(
                method = 'purge',
                mailbox = str(mailbox),
        )

    def prompt(self, prompt, **kwargs):
        if 'dnid' in kwargs:
            arg = dict((('dnid', kwargs['dnid']),))
        elif 'extension' in kwargs:
            arg = dict((('extension', kwargs['extension']),))
        else:
            return None
        return self.make_query(
                method = 'prompt',
                prompt = prompt,
                **arg
        )

    def play(self, prompt, **kwargs):
        if 'dnid' in kwargs:
            arg = dict((('dnid', kwargs['dnid']),))
        elif 'extension' in kwargs:
            arg = dict((('extension', kwargs['extension']),))
        else:
            return None
        return self.make_query(
                method = 'play',
                prompt = prompt,
                **arg
        )

    def transfer(self, uid, extension):
        return self.make_query(
                method = 'transfer',
                uid = str(uid),
                extension = str(extension),
        )

    def set_var(self, variable, value):
        return self.make_query(
                method = 'set',
                variable = str(variable),
                value = str(value),
        )

    def get_var(self, variable):
        return self.make_query(
                method = 'get',
                variable = str(variable),
        )
