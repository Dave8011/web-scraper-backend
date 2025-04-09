from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_title
import os

app = Flask(__name__)
CORS(app)  # ✅ Allow frontend (e.g., Vercel) to access this API

@app.route('/')
def home():
    return "Backend is alive!"

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json(force=True)
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL not provided'}), 400

    result = scrape_title(url)

    # If it's a dict with error, return it with 500 status
    if isinstance(result, dict) and result.get("error"):
        return jsonify(result), 500

    # ✅ Return structured info
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

