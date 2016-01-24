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

"""
#takes in a json data structure and interprets it to perform the desired action
def acceptCommand(data):
        option_choice = data.get("option")
        positions = data.get("positions") #positions of the LEDs that we wish to change
        color = data.get("color") #tuple representing the color that the desired LEDs should be changed to
        
        if option_choice == "refresh": 
                return boardState.getMatrix() #get the most recent state of the board
        elif option_choice == "setStartColor":
                boardState.setStartColor(color) #set the entire board to be "color"
        elif option_choice == "setBackgroundColor":
                pass
        else:
                pass
"""
                
        
