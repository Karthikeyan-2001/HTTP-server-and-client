#HTTP SERVER

#Imports
from http.server import BaseHTTPRequestHandler, HTTPServer

#Create custom HTTPRequestHandler class
class WebServerHandler(BaseHTTPRequestHandler):

    #handle GET command
    def do_GET(self):
        rootdir = r'C:/Users/HOME/Desktop/CN/Exp 2/' #file location (give html files location to send to client)
        try:
            if self.path.endswith(".html") or self.path.endswith(".txt"):
                f = open(rootdir + self.path) #open requested file

                self.send_response(200)  #send code 200 response

                self.send_header('Content-type', 'text/html')  #send header first
                self.end_headers()

                #send file content to client
                self.wfile.write(bytes("<html><head>THE GROUP-2</title></head>", "utf-8"))
                self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
                self.wfile.write(bytes("<body>", "utf-8"))
                self.wfile.write(bytes("<p>Content in Requested File:</p>", "utf-8"))
                self.wfile.write(bytes(f"<p>{f.read()}</p>", "utf-8"))
                self.wfile.write(bytes("</body></html>", "utf-8")) 
                f.close()
                return

        # If file not Found
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        host = '127.0.0.1'
        port = 8080
        server = HTTPServer((host, port), WebServerHandler) 
        print("Server started http://%s:%s" % (host, port))  
        server.serve_forever()  # Starting the server
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....!") #To stop the server
        server.socket.close()

if __name__ == '__main__':
    main()