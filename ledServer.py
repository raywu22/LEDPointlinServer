from webHandler import piHandler
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

def main():
	try:
		server = HTTPServer(('',3000), piHandler)
		print 'started httpserver...'
		server.serve_forever()
	except:
		print 'shutting down'
		server.socket.close()

if __name__ == '__main__':
	main()
