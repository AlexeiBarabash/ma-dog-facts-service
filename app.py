from flask import Flask
import requests , json, random, os

app = Flask(__name__)

@app.route("/")
def get_fact():
  url = requests.get(s.environ.get('DATA_URL'))
  fact = random.choice(json.loads(url.text))
  return fact["fact"]

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)