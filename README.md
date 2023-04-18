# HTTP-Fingerprinting-Server

This http server logs all header and client information from GET request.
Additionally the HTML that is hosted contains JS which will POST additional data about the browsers capabilities back to the server:

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

and more.

## Target Whitelisting
Add IP v4 and v6 addresses to the whitelist.txt file to target the logs and to reduce noise from bots and crawlers.

### Formatting
IP v4 and v6 addresses in CIDR notation and new line deliniated.

File should be should be formatted as follows:

IPv4/CIDR

IPv4/CIDR

IPv6/CIDR

IPv4/CIDR

