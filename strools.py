import stravalib, cherrypy

class getToken(object):
    token = None
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
        self.token = client.exchange_code_for_token(client_id=self.CLIENT_ID,client_secret=self.SECRET,code=code)
        print "Token : {} - Rights : {}".format(self.token,self.SCOPE)
        cherrypy.engine.exit()


def get_token(client_id, secret, scope='view_private'):
    Tok = getToken(client_id, secret, scope)
    conf = {
        '/': { },
    }
    cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 8181})
    cherrypy.quickstart(Tok, '/', conf)
    return Tok.token
