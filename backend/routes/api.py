try:
    from flask import Flask, jsonify
except ImportError:
    Flask = None
    jsonify = None


def create_app():
    if Flask is None:
        raise RuntimeError("Flask is not installed. Run pip install -r requirements.txt")

    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    return app
