import flask
import json
from flask import jsonify
from flask import request
from BoardState import BoardState

app = flask.Flask(__name__)

boardState = BoardState((0,0,0),70,70)


@app.route('/')
def index():
        return "hi"

@app.route('/boardData', methods=['POST'])
def boardData():
        #print hi.body
        dataJSON = json.loads(request.data)
        option_choice = dataJSON["option"]        
        if option_choice == "refresh":
                return jsonify(data = boardState.getMatrix())
        elif option_choice == "setStartColor":
                color = dataJSON["color"]
                boardState.setStartColor(color) #set the entire board to be "color"
        elif option_choice == "setBackgroundColor":
                color = dataJSON["color"]
                boardState.setBackground(color)
        elif option_choice == "setColorAtIndices":
                color = dataJSON["color"]
                indices = dataJSON["indices"]
        	for index in indices:
        		boardState.setColorSingleIndex(index,color)
        elif option_choice == "reset":
        	boardState.reset() #resets entire board to startColor
        elif option_choice == "erase":
                indices = dataJSON["indices"]
        	for index in indices:
        		boardState.reset(index) #resets LEDs at the desired indices only
        elif option_choice == "scaleBrightness":
        	scale = dataJSON["scale"] #int representing the scaling factor
        	boardState.scaleBrightness(scale) #scale entire board's brightness
        else:
                return jsonify(data = boardState.getMatrix())
        
        #a = boardState.getMatrix()
        #return ','.join(str(r) for v in a for r in v)
        return jsonify(data = boardState.getMatrix())

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


#takes in a json data structure and interprets it to perform the desired action
def acceptCommand(data):
        #dataJSON = json.loads(data)
        print "hi"
        return "hi"
        """
        if option_choice == "refresh": 
                return boardState.getMatrix() #get the most recent state of the board
        elif option_choice == "setStartColor":
                boardState.setStartColor(color) #set the entire board to be "color"
        elif option_choice == "setBackgroundColor":
                pass
        else:
                pass
        """
        

                
        
