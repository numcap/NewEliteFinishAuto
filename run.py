"""
Elite Finish Auto - local preview server.

HOW TO USE IN PYCHARM:
  1. Put this file inside the elitefinishauto folder (same place as index.html).
  2. Open the folder in PyCharm (File > Open).
  3. Open this file, then click the green Run button (or right-click > Run 'run').
  4. Your browser opens at http://localhost:8000
  5. To stop the server, click the red Stop square in PyCharm (or press Ctrl+C).

No installs needed - this only uses Python's built-in modules.
"""

import http.server
import os
import socketserver
import webbrowser

PORT = 8000

# Serve files from the folder this script lives in, no matter where PyCharm runs it from.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    handler = http.server.SimpleHTTPRequestHandler
    # allow_reuse_address avoids "address already in use" if you restart quickly
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print("=" * 52)
        print("  Elite Finish Auto is running")
        print(f"  Open: {url}")
        print("  Stop: click the red Stop square (or press Ctrl+C)")
        print("=" * 52)
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
