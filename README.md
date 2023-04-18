# HTTP-Fingerprinting-Server

A Python3 web server that allows only targeted IPs and attempts to fingerprint the incoming requests by capturing connection and browser information. 

The hosted HTML contains JS which will POST additional data about the browsers capabilities back to the server.

![fingerprinting_server_diagram](https://user-images.githubusercontent.com/6628565/232662379-f3f4015f-94fc-41b4-834c-08e4aa12cd89.png)

## Logged Data
- IP
- sec-ch-ua
- sec-ch-ua-mobile
- sec-ch-ua-platform
- DNT
- userAgent
- screenResolution
- installedFonts
- browserPlugins
- timezone
- language
- colorDepth
- platform
- User Activity via mousemoved js event listener

and more.

## Setup

- Place a __whitelist.txt__ file at the root of the project and populate it with IPv4 or 6 address ranges in CIDR notation (/24) and _new line deliniated_.

- Set a __GUID__ for the __GET__ handler, __POST__ handler, and in the __sample_site.html__ postback.

- Send a link to the target and wait to see target details in the ```access.log``` file.

## Target Scoping

### Whitelisting

Add IP v4 and v6 addresses to the whitelist.txt file to target the logs and to reduce noise from bots and crawlers.

### GUID for Routes

Using GUIDs for GET and POST routes will greatly reduce the number of bots and crawlers hitting your endpoints and dirtying up the logs. 
