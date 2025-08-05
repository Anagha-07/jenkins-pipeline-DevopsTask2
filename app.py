from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h2 style="color:green;">✅ SUCCESS</h2>
    <p>🚀 Hello from <strong>Jenkins Pipeline!</strong></p>
    <p>📦 Build & Deployment Completed</p>
    """

@app.route('/health')
def health():
    return """
    <h3>Health Check</h3>
    <ul>
        <li>Status: <strong>UP</strong></li>
        <li>Service: Flask Jenkins Demo</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
