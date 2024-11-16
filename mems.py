# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Example function to generate citation in APA format
def generate_apa_citation(author, title, year, journal, url):
    return f"{author} ({year}). {title}. *{journal}*. Retrieved from {url}"

@app.route('/generate_citation', methods=['GET'])
def generate_citation():
    # Get parameters from the URL
    author = request.args.get('author', 'Unknown Author')
    title = request.args.get('title', 'Unknown Title')
    year = request.args.get('year', 'n.d.')
    journal = request.args.get('journal', 'Unknown Journal')
    url = request.args.get('url', 'https://example.com')

    # Generate APA citation
    citation = generate_apa_citation(author, title, year, journal, url)

    return jsonify({
        "format": "APA",
        "citation": citation
    })

if __name__ == '__main__':
    app.run(debug=True)
