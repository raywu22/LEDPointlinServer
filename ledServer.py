import flask
from BoardState import BoardState

app = flask.Flask(__name__)

boardState = BoardState((0,0,0),70,70)


@app.route('/')
def index():
        return "hi"

@app.route('/boardData', methods=['POST'])
def boardData():
        print boardState.getMatrix()
        return "hello"

if __name__=="__main__":
        app.run(None,3000,None)

"""
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
"""

