from flask import Flask, request, jsonify
from scraper import scrape_title

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL not provided'}), 400

    title = scrape_title(url)
    return jsonify({'title': title})

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify
from scraper import scrape_data

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    scraped_data = scrape_data(url)
    return jsonify({'result': scraped_data})

if __name__ == '__main__':
   import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

