from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

app = Flask(__name__)

def detect_outlet(url):
    """Detect which news outlet the URL is from"""
    parsed = urlparse(url)
    domain = parsed.netloc.lower().replace('www.', '')
    
    if 'bbc' in domain:
        return 'bbc'
    elif 'newyorker' in domain:
        return 'newyorker'
    else:
        return 'generic'

def extract_article_bbc(soup):
    """Extract article content and images from BBC"""
    article = soup.find('article')
    if not article:
        return None, "No article tag found"
    
    content = []
    images = []
    
    for element in article.descendants:
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            heading_text = element.get_text(strip=True)
            if heading_text:
                content.append({
                    'type': 'heading',
                    'level': level,
                    'text': heading_text
                })
        
        elif element.name == 'p':
            paragraph_text = element.get_text(strip=True)
            if paragraph_text:
                content.append({
                    'type': 'paragraph',
                    'text': paragraph_text
                })
        
        elif element.name == 'img':
            img_src = element.get('src', '')
            img_alt = element.get('alt', 'Article image')
            if img_src and img_src.startswith('http'):
                images.append({
                    'src': img_src,
                    'alt': img_alt
                })
    
    return {'content': content, 'images': images}, None

def extract_article_newyorker(soup):
    """Extract article content and images from The New Yorker"""
    article = soup.find('article')
    if not article:
        return None, "No article tag found"
    
    content = []
    images = []
    seen = set()  # Track seen elements to avoid dupes
    
    for element in article.descendants:
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            heading_text = element.get_text(strip=True)
            if heading_text and heading_text not in seen:
                content.append({
                    'type': 'heading',
                    'level': level,
                    'text': heading_text
                })
                seen.add(heading_text)
        
        elif element.name == 'p':
            paragraph_text = element.get_text(strip=True)
            if paragraph_text and paragraph_text not in seen:
                content.append({
                    'type': 'paragraph',
                    'text': paragraph_text
                })
                seen.add(paragraph_text)
        
        elif element.name == 'img':
            img_src = element.get('src', '')
            img_alt = element.get('alt', 'Article image')
            # New Yorker uses relative URLs and CDNs
            if img_src and not 'logo' in img_src.lower() and not 'svg' in img_src.lower():
                if not img_src.startswith('http'):
                    img_src = 'https://www.newyorker.com' + img_src
                images.append({
                    'src': img_src,
                    'alt': img_alt
                })
    
    return {'content': content, 'images': images}, None

def extract_article_generic(soup):
    """Extract article content and images from generic outlets"""
    article = soup.find('article')
    if not article:
        return None, "No article tag found"
    
    content = []
    images = []
    
    for element in article.descendants:
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            heading_text = element.get_text(strip=True)
            if heading_text:
                content.append({
                    'type': 'heading',
                    'level': level,
                    'text': heading_text
                })
        
        elif element.name == 'p':
            paragraph_text = element.get_text(strip=True)
            if paragraph_text:
                content.append({
                    'type': 'paragraph',
                    'text': paragraph_text
                })
        
        elif element.name == 'img':
            img_src = element.get('src', '')
            img_alt = element.get('alt', 'Article image')
            if img_src and img_src.startswith('http'):
                images.append({
                    'src': img_src,
                    'alt': img_alt
                })
    
    return {'content': content, 'images': images}, None

def extract_article(url):
    """Extract article content and images from the given URL"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return None, f"Error fetching URL: {str(e)}"
    
    outlet = detect_outlet(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if outlet == 'bbc':
        result, error = extract_article_bbc(soup)
    elif outlet == 'newyorker':
        result, error = extract_article_newyorker(soup)
    else:
        result, error = extract_article_generic(soup)
    
    if error:
        return None, error
    
    return {'content': result['content'], 'images': result['images'], 'outlet': outlet}, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-article', methods=['POST'])
def fetch_article():
    url = request.form.get('url', '').strip()
    
    if not url:
        return render_template('article.html', 
                             error="Please enter a URL")
    
    # Handle URL without protocol
    if not url.startswith('http'):
        url = 'https://' + url.split('//')[-1]
    
    article_data, error = extract_article(url)
    
    if error:
        return render_template('article.html', error=error)
    
    return render_template('article.html', 
                         article=article_data['content'],
                         images=article_data['images'],
                         outlet=article_data['outlet'],
                         url=url)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)