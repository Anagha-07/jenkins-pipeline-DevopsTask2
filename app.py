from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h2 style="color:green;">✅ SUCCESS</h2>
    <p>🚀 Hello from <strong>Jenkins CI/CD Pipeline!</strong></p>
    <p>📦 Build & Deployment Completed</p>
    <p>🔁 Auto Build via GitHub Webhook</p>
    <p><a href='/health'>Check Health</a> | <a href='/info'>App Info</a></p>
    """

@app.route('/health')
def health():
    return """
    <h3>🩺 Health Check</h3>
    <ul>
        <li>Status: <strong style='color:green;'>UP</strong></li>
        <li>Service: Jenkins Flask Demo</li>
    </ul>
    """

@app.route('/info')
def info():
    return f"""
    <h3>ℹ️ App Info</h3>
    <ul>
        <li>App Name: Jenkins Flask Demo</li>
        <li>Version: 1.0.0</li>
        <li>Author: Anagha</li>
        <li>Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</li>
    </ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
