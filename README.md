# Strools
THE "strava-tools" library.

##getToken
Get your token to use with stravalib API.

###Usage :
```python
import cherrypy, strools
cherrypy.quickstart(strools.getToken(client_id,secret,scope))

