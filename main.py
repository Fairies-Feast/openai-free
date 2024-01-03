import os
os.system("pip install flask g4f flask-cors")
from flask import Flask, request
import g4f
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/chat', methods=['GET'])
def chat():
  try:
    # Get parameters from the request URL
    query_message = request.args.get('query', '')
    query_message = base64.b64decode(query_message)
    query_message = query_message.decode()
    # Using ChatCompletion for chat models
    response = g4f.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": query_message}],
      stream=True,
    )
    # Iterate over the response and send each message as part of the response
    result = ''.join(message for message in response)
    
    return str(result)
  except:
    return "error"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
