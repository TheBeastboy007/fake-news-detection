from newspaper import Article

def scrape_news(url):
    """Scrapes a single news article from a URL."""
    article = Article(url)
    article.download()
    article.parse()
    return {
        "title": article.title,
        "source": article.source_url,
        "content": article.text,
        "published_at": article.publish_date
    }

# Example usage:
if __name__ == "__main__":
    url = "https://www.bbc.com/news/world-61767774"
    news_data = scrape_news(url)
    print(news_data)
