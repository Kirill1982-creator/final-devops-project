from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = f"<h1>🚀 DevOps Final Project</h1><p>Time: {datetime.datetime.now()}</p><p>Status: OK</p>"
        self.wfile.write(html.encode())

if __name__ == "__main__":
    HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
