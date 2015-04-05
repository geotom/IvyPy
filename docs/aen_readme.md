Application Event Notifications
===
###Documentation from Ironvoice

With the Application Event Notifications settings you can connect our service to your applications using simple web services.

> Note: Your application developer will know how to complete your side of the integration.

* Host - Your internet accessible web server
* Secure - Check if your web server is configured to use SSL
* Path - The path to the page on your web server that will handle the request

Event Notifications
---

Our service can be configured to notify your web based application in real-time with the following events:

| Event | Parameters |
|---|---|
| inbound | uid, cid, dnid |
| answered | uid, cid, dnid, extension |
| outbound | uid, cid, dnid, extension |
| hangup | uid, cid, dnid |

> Note: With the passive nature of our design, call flow will not be affected if your server cannot be reached.

As an example for an inbound call the complete POST might look like this:

`https://<server>/<path>?event=inbound&uid=1368018803.329176&cid=2055551234&dnid=8005884096`

Application Event Feed
---

You can poll real-time call status using your API server and key:

`https://<server>/aen?key=<key>`

Will return a list of current calls:

````
2013-07-10 11:49:17,outbound,1373474957.179327,2055884096,2055551234,805
2013-07-10 11:50:08,inbound,1373474957.179327,2055884096,2055551234,805
2013-07-10 11:45:52,answered,1373474957.179327,2055884096,2055551234,888
````
