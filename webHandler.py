import string,cgi
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from BoardState import BoardState

class piHandler(BaseHTTPRequestHandler):
        def __init__(self):
                self.boardState = BoardState(0,70,70)
                
	def do_GET(self):
		try:
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write('you did it!')
			return
		except IOError:
			self.send_error(404,'you messed up')
	
	def do_POST(self):
		#global rootnode
		try:
			ctype,pdict = cgi.parse_header(self.headers.getheader('content-type'))
			print "ctype: ",ctype
			print "pdict: ",pdict
                        if ctype == 'multipart/form-data':
                                bodyData = cgi.parse_multipart(self.rfile, pdict)
                        elif ctype == 'application/x-www-form-urlencoded':
                                length = int(self.headers.getheader('content-length'))
                                bodyData = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
                        else:
                                bodyData = {}
                        print bodyData
			self.send_response(301)
			self.end_headers()
			print self
			self.wfile.write('hihi')
			print 'done'
		except:
			print 'Wrong Data Structure'
			pass
