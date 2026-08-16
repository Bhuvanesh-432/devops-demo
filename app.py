from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello DevOps!"


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    # 0.0.0.0 means "listen on all network interfaces", not just localhost.
    # This is required so Docker can expose this port to the outside world.
    app.run(host="0.0.0.0", port=5000)
