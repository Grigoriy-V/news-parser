import requests
from bs4 import BeautifulSoup
import pandas as pd

class NewsParser:
    def __init__(self, config):
        self.urls = config.get('source_urls', [])
        self.output = config.get('output_path')
        self.headers = {'User-Agent': config.get('user_agent', '')}

    def fetch(self, url):
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        return resp.text

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        articles = []
        for item in soup.select('article'):
            title = item.select_one('h2').get_text(strip=True)
            link = item.select_one('a')['href']
            articles.append({'title': title, 'url': link})
        return articles

    def run(self):
        all_articles = []
        for url in self.urls:
            html = self.fetch(url)
            articles = self.parse(html)
            all_articles.extend(articles)
        df = pd.DataFrame(all_articles)
        df.to_csv(self.output, index=False)
        print(f'Saved {len(all_articles)} articles to {self.output}')
