import cherrypy


class AenHost(object):
    @cherrypy.expose
    def index(self, event, uid, cid, dnid, extension=None):
        return 'AEN Okay'

if __name__ == '__main__':
    cherrypy.tree.mount(AenHost(), '/aen', 'aen_conf')

    cherrypy.engine.start()
    cherrypy.engine.block()
