from ddtrace import tracer

"""
tracer.configure(
    hostname='datadog',
    port=8126,
)
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is Flask running in a Docker container.'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
