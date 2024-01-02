from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

if __name__ == '__main__':
    app.run(ssl_context=('certificate.crt', 'privateKey.key'), host='0.0.0.0', port=443)
