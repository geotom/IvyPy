# IvyPy
Python server (CherryPy) and tools for the IronVoice API.

##Module: ironvoiceapi.py
Provides access to the IronVoice REST API, defined as follows:


Note: Depending on your plan some methods may not be available.
Reference

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

Variable 	Values 	Description
afterhours 	1,0 	Enable or disable after hours mode
Example Usage

https://<server>/api?key=<key>&method=call&dnid=2055551234&extension=801

Response

A JSON object will be returned with the requested data or "OK" if the operation was performed successfully.
