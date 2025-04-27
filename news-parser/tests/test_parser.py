import pytest
from parser.parser import NewsParser

@pytest.fixture
def sample_html():
    return """
    <html><body>
      <article><h2>Title1</h2><a href=\"/link1\">Read more</a></article>
      <article><h2>Title2</h2><a href=\"/link2\">Read more</a></article>
    </body></html>
    """

@pytest.fixture
def config(tmp_path):
    return {
        'source_urls': [],
        'output_path': str(tmp_path / 'out.csv'),
        'user_agent': 'test'
    }


def test_parse(sample_html, config):
    np = NewsParser(config)
    articles = np.parse(sample_html)
    assert len(articles) == 2
    assert articles[0]['title'] == 'Title1'
