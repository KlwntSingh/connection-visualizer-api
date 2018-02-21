from flask import Flask, render_template, jsonify
app = Flask(__name__)
from dao import get_ip_address_info

@app.route("/info/<ip>")
def ip_info(ip):
   #print(get_ip_address_info(ip))
   return jsonify(get_ip_address_info(ip))

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=3000)