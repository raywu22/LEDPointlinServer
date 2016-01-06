import string,cgi
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class piHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			self.send_response(200)
			self.send_header('Content-type',	'text/html')
			self.end_headers()
			self.wfile.write('you did it!')
			return
		except IOError:
			self.send_error(404,'you fucked up')
	
	def do_POST(self):
		#global rootnode
		try:
			ctype,pdict = cgi.parse_header(self.headers.getheader('content-type'))
			print ctype
			self.send_response(301)
			self.end_headers()
			self.wfile.write('hihi')
			print 'done'
		except:
			print 'pass'
			pass
