import cherrypy

class DisplayStatus(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

class StatusWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        


if __name__ == '__main__':
    conf = { 
        '/': {
             'tools.sessions.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd()),
        },
        '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': './public'.
        },
    }

    webapp = DisplayStatus()
    cherrypy.quickstart(webapp, '/', conf)
