import os
import subprocess
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK')
    
    def log_message(self, format, *args):
        pass

def start_healthcheck():
    port = int(os.environ.get('PORT', 80))
    server = HTTPServer(('0.0.0.0', port), HealthHandler)
    print(f"✅ Healthcheck running on port {port}")
    server.serve_forever()

def start_v2ray():
    print("✅ V2Ray starting on port 8080...")
    subprocess.run(['/usr/local/bin/v2ray', 'run', '-c', '/etc/v2ray/config.json'])

if __name__ == '__main__':
    print("🚀 Starting V2Ray VPN Server...")
    
    # Start healthcheck in background
    t = threading.Thread(target=start_healthcheck, daemon=True)
    t.start()
    
    # Start V2Ray in main thread
    start_v2ray()
