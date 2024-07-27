from news_summarize import summarize_news_article

# def format_news(news_headlines):
#     formatted_news = ""
#     for article in news_headlines['articles'][:2]:  # Limiting to top 2 articles
#         title = article['title']
#         # description = article['description']
#         url = article['url']
#         formatted_news += f"<p><strong>{title}</strong></p><p><a href='{url}' target='_blank'>Read more</a></p>"
#     return formatted_news.strip()

def news(news_headlines):
    formatted_news = ""
    for article in news_headlines['articles'][:2]:  # Limiting to top 2 articles
        title = article['title']
        # description = article['description']
        url = article['url']
        formatted_news += f"<p><strong>{title}</strong></p><p><a href='{url}' target='_blank'>Read more</a></p>"
    return formatted_news.strip()