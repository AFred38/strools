# Strools
THE "strava-tools" library.

##getToken
Get your token to use with stravalib API.

###Usage :
```python
import strools
tok = strools.get_token(client_id, secret, scope)
```
If `scope` is not given, the default value `view_private` is used.


