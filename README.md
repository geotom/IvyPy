# IvyPy

Python server (CherryPy) and tools for the IronVoice API.

## Requirements

See [requirements.txt](requirements.txt), because Virtualenv and `pip install -r requirements.txt` are your friends.

## Module: ironvoiceapi.py

Provides a _very_ thin wrapper around the IronVoice REST API.  Each IronVoice API method is represented in the `ivapi` class, which will accept almost any argument and try to give back _something_ (even if it's nothing) without raising an error.  First it will try to parse any response as JSON and return it as a Python dictionary.  Then it will try to return the bare response. Lastly, it will return `None` upon failure.

Creation of the `ivapi` class requires either passing of a valid host and API key, or the module must be able to import a valid ironvoiceapi_conf.py file, which looks like this:

    host = ''  # Example: 'http://foo.ironvoice.com'  The protocol (the http: part) _is_ required
    key = ''  # Your IronVoice API key, available under the Global Settings menu of the IronVoice site

#### Example Usage

    >>>import ironvoiceapi
    >>>iva = ironvoiceapi.ivapi(
        host = 'http://foo.ironvoice.com',
        key = '*************************'
        )
    >>>peers = iva.peers()
    >>>print peers['800']
    {'ip': '127.0.0.1', 'ping': '91', 'port': '1037'}

#### IronVoice API Reference

Note: Depending on your plan some methods may not be available.

Method | Parameters | Description
-------|------------|------------
trace |	host |	Returns hops and latency from our network to the specified host
peers | |	Returns the registration status, ip address, and latency of extensions
recording |	uid |	Returns url and file size of the specified call recording
recordings |	extension |	Returns instant call recordings for the specified extension, includes urls to recordings
call |	dnid, extension, cid |	Establishes a call to the specified number and then connects the specified extension
fax | |	Returns a list of received faxes, includes urls to documents
inbox |	mailbox |	Returns message count for specified mailbox
voicemail |	mailbox |	Returns contents of the specified mailbox, includes urls to messages
archive |	mailbox, message |	Archives the specified message for the specified mailbox
cleanup |	mailbox |	Archives all messages for the specified mailbox
purge |	mailbox |	Permanently removes all messages from the specified mailbox and its archive
prompt | dnid or extension, prompt |	Establishes a call to the specified number or extension and then records the prompt
play |	dnid or extension, prompt |	Establishes a call to the specified number or extension and then plays the prompt
transfer |	uid, extension |	Transfers a call with the specified uid to the specified extension
set |	variable,value |	Sets a variable with the specified value
get |	variable |	Gets the value of the specified variable

Variable |	Values |	Description
---------|---------|-------------
afterhours |	1,0 |	Enable or disable after hours mode

