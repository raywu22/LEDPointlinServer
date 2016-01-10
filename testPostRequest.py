import requests

#p = requests.get("http://localhost:3000")
reqDict = {"key":"value","key1":"value1"}
r = requests.post("http://localhost:3000/boardData", data = reqDict)

print r.text
