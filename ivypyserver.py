import cherrypy


class Root(object):
    @cherrypy.expose
    def extension(self, ext = None):
        return str(ext)

if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/')
