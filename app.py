from flask import Flask
import requests , json, random

app = Flask(__name__)

@app.route("/")
def get_fact():
  url = requests.get("http://ma-dog-sources-service-ma-services.default.svc.cluster.local:5000/api/v1/resources/dogs/all")
  fact = random.choice(json.loads(url.text))
  return fact["fact"]

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)