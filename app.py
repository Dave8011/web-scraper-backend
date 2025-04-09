from flask import Flask, request, jsonify
from scraper import scrape_title
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend is alive!"

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json(force=True)
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL not provided'}), 400

    title = scrape_title(url)
    return jsonify({'title': title})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
