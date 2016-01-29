import requests
import json
#p = requests.get("http://localhost:3000")
reqDict = json.dumps({"option":"setColorAtIndices","color":(19,2,0),"indices":[[0,0],[1,2]]})

r = requests.post("http://localhost:3000/boardData", data = reqDict)

#print r.text


#[((x,y),(r,g,b)),((x1,y1),(r1,g1,b1))]
