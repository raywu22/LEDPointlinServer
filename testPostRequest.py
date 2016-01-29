import requests
import json
#p = requests.get("http://localhost:3000")
reqDict = json.dumps({"option":"refresh"})

r = requests.post("http://localhost:3000/boardData", data = reqDict)

print r.text


#[((x,y),(r,g,b)),((x1,y1),(r1,g1,b1))]
