from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'v5.0.0 - Fixed version'  # Pretend this is broken

app.run(host='0.0.0.0', port=8080)
