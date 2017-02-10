import stravalib, cherrypy

class getToken(object):
    def __init__(self, client_id, secret,scope):
        self.CLIENT_ID = client_id
        self.SECRET = secret
        self.SCOPE = scope

    @cherrypy.expose
    def index(self):
        client = stravalib.Client()
        url = client.authorization_url(client_id=self.CLIENT_ID, scope=self.SCOPE,
        redirect_uri='http://localhost:{}/authorize'.format(cherrypy.server.socket_port))
        raise cherrypy.HTTPRedirect(url)

    @cherrypy.expose
    def authorize(self,state=None,code=None):
        client = stravalib.Client()
        token = client.exchange_code_for_token(client_id=self.CLIENT_ID,client_secret=self.SECRET,code=code)
        print "Token : {} - Rights : {}".format(token,self.SCOPE)
        return token
        
