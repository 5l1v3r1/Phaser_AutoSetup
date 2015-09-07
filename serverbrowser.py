import http.server
import webbrowser

def open_browser():
    new=1
    url = "http://127.0.0.1:8000"
    httpd = http.server.HTTPServer(('localhost', 8000), http.server.SimpleHTTPRequestHandler)
    print("Server setup successfully! Serving on locolhost on port 8000.")
    webbrowser.open(url, new=new)
    httpd.serve_forever()
