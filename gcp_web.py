#!/usr/bin/env python
from PIL import Image
import cherrypy
import rospy
from geometry_msgs.msg import PoseStamped
import threading
import os
config = {
    'global' : {
        'server.socket_host' : '192.168.3.9',
        'server.socket_port' : 8081
    }
}
class HelloWorld(object):
    def __init__(self):
        print("hihi")
    @cherrypy.expose
    def index(self):

        # <input type="button" value="goalA" onclick="location.href='192.168.3.3:8080/goalA_to'">
        # ERIC https://github.com/VirtuosoEric/robot_web_service/blob/pn60/home.html
        
        f = open("gcp_picture.html", "r")
        return f

    @cherrypy.expose
    def upload(self, ufile):
        # Either save the file to the directory where server.py is
        # or save the file to a given path:
        # upload_path = '/path/to/project/data/'
        upload_path = os.path.dirname(__file__)
        print(upload_path)
        # Save the file to a predefined filename
        # or use the filename sent by the client:
        # upload_filename = ufile.filename
        upload_filename = 'saved.png'

        upload_file = os.path.normpath(
            os.path.join(upload_path, upload_filename))
        size = 0
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)
        out = '''
File received.
Filename: {}
Length: {}
Mime-type: {}
''' .format(ufile.filename, size, ufile.content_type, data)
        return out

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld(), '/',config)
    