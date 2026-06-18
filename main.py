from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'v6.0.0 - Broken version again'  # Pretend this is broken

app.run(host='0.0.0.0', port=8080)
