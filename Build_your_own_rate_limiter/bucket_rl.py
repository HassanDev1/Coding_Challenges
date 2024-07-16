from flask import Flask,jsonify,request,Response
import time

app = Flask(__name__)
CAPACITY_TOKEN = 10
TOKEN_REFILL_RATE= 1

buckets = {}

def refill_tokens(ip):
    bucket = buckets[ip]
    now = time.time()
    elapsed = now - bucket["last_refill"]
    added_tokens = (elapsed*TOKEN_REFILL_RATE)
    if added_tokens > 0:
        bucket["tokens"] = min(CAPACITY_TOKEN,bucket["tokens"]+added_tokens)
        bucket["last_refill"] = now


#End point with limited request
@app.route("/limited",methods=["GET"])
def limited():
    ip = request.remote_addr
    if ip not in buckets:
        buckets[ip] = {
            "tokens":CAPACITY_TOKEN,
            "last_refill":time.time()
        }

    refill_tokens(ip)
    if buckets[ip]["tokens"] > 0:
        buckets[ip]["tokens"] -= 1
        
        return jsonify({"message":"Request successful"})
    else:
        return Response("Too many Request",status=429)

#Endpoint with unlimited request
@app.route("/unlimited",methods=["GET"])
def unlimited():
    return jsonify({"message":"This endpoint is unlimited"})







if __name__ == "__main__":
    app.run(debug=True)