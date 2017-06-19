from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index(): 
    return jsonify(cpuserial=getSerial())
	
def getSerial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
  return cpuserial

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')