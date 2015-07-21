from flask import Flask, request, redirect, url_for, send_from_directory, send_file

app = Flask(__name__)

# Routes
@app.route('/')
def root():
    return send_file('flask-docker.png', mimetype='image/png')

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
