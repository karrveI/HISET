import http.server
import socketserver
import threading

Handler = http.server.SimpleHTTPRequestHandler

class Server():
    def __init__(self, PORT):
        self.httpd = socketserver.TCPServer(("", PORT), Handler)

    #start the server
    def start_server(self):
        threading.Thread(target=self.httpd.serve_forever).start()

    #stop the server
    def stop_server(self):
        self.httpd.shutdown()
        self.httpd.server_close()
