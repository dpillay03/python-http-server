from http.server import HTTPServer, BaseHTTPRequestHandler
import csv

with open('./data.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()
