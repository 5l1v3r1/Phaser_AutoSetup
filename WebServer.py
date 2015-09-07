import http.server

def server_setup():
   httpd = http.server.HTTPServer(('localhost', 8000), http.server.SimpleHTTPRequestHandler)
   print("Server setup successfully! Serving on locolhost on port 8000.")
   httpd.serve_forever()
   
server_setup()
