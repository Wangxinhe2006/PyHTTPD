from http.server import BaseHTTPRequestHandler, HTTPServer
from os.path import abspath

class PyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if abspath(self.path[1:]).index(abspath('.')):
				raise ValueError
			f = open(self.path[1:], 'r')
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(f.read().encode())
			f.close()
		except ValueError:
			self.send_error(403, 'Forbidden: %s' % self.path)
		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)

def main():
	try:
		server = HTTPServer(('', 80), PyHandler)
		print('Welcome to the machine...'),
		print('Press ^C once or twice to quit.')
		server.serve_forever()
	except KeyboardInterrupt:
		print('^C received, shutting down server')
		server.socket.close()

if __name__ == '__main__':
	main()
