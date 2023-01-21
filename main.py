import requests
from flask import Flask, jsonify,request
app = Flask(__name__)
@app.route('/md5.php', methods=['POST','GET'])
def crack():
    return "//open/"

@app.errorhandler(404)
def not_found(error):
    return '{"ok":true,"code":200,"message":"Successful","forever":true,"timestamp":1705843020,"datetime":"2024-01-21T13:17:00.717781Z"}'

context = ('serf.crt', 'key.key')#cs
app.run(debug=True,host="0.0.0.0",port=443,ssl_context=context)




