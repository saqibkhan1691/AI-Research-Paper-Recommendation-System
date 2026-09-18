"""
AI Research Paper Recommendation System - Backend Server
Author: SHAKI-cell
"""

import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# ─────────────────────────────────────────────
# Configuration from environment variables
# ─────────────────────────────────────────────
PORT = int(os.getenv("PORT", 5000))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///papers.db")
ARXIV_API_URL = os.getenv("ARXIV_API_URL", "http://export.arxiv.org/api/query")
SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "")

app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL


# ─────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────

@app.route("/", methods=["GET"])
def home():
    """Health check endpoint."""
    return jsonify({
        "status": "running",
        "message": "AI Research Paper Recommendation System API",
        "port": PORT
    })


@app.route("/api/search", methods=["GET"])
def search_papers():
    """Search papers by query."""
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "Query parameter 'q' is required."}), 400

    # TODO: Integrate with arXiv / Semantic Scholar / CrossRef APIs
    return jsonify({
        "query": query,
        "results": [],
        "message": "Search endpoint ready. API integration pending."
    })


@app.route("/api/recommend", methods=["POST"])
def recommend_papers():
    """Generate personalized paper recommendations for a user."""
    data = request.get_json()
    if not data or "user_id" not in data:
        return jsonify({"error": "user_id is required in request body."}), 400

    user_id = data["user_id"]

    # TODO: Connect to recommendation engine (NLP/ML processing)
    return jsonify({
        "user_id": user_id,
        "recommendations": [],
        "message": "Recommendation engine ready. ML model integration pending."
    })


@app.route("/api/feedback", methods=["POST"])
def submit_feedback():
    """Submit user feedback (like/dislike/bookmark) for a paper."""
    data = request.get_json()
    required_fields = ["user_id", "paper_id", "rating"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"'{field}' is required."}), 400

    # TODO: Store feedback in database and update user profile
    return jsonify({
        "message": "Feedback recorded successfully.",
        "data": data
    })


@app.route("/api/health", methods=["GET"])
def health_check():
    """Detailed health check."""
    return jsonify({
        "status": "healthy",
        "port": PORT,
        "debug": DEBUG,
        "database": DATABASE_URL.split("://")[0] if DATABASE_URL else "not configured"
    })


# ─────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print(f"[INFO] Starting server on port {PORT} (debug={DEBUG})")
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
