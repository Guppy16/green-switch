from flask import Flask
import octopus_energy
from flask import jsonify
from flask import json

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulations, it's a web app!"

@app.route("/products")
def get_products():
  """
  Return list products from octopus energy
  """
  energy_prods = octopus_energy.get_energy_products()
  return jsonify(energy_prods)

@app.route("/test")
def test():
  a = [1,2]
  return json.dumps(a)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)