# HTTP-Fingerprinting-Server

This http server logs all header and client information from GET request.
Additionally the HTML that is hosted contains JS which will POST the following back to the server:
- userAgent
- screenResolution
- installedFonts
- browserPlugins
- timezone
- language
- colorDepth
- platform

