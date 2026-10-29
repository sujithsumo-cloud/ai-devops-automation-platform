from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "AI-Powered DevOps Automation and Intelligence Platform",
        "message": "Application is running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )
