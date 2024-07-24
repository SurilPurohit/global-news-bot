from news_summarize import summarize_news_article

def format_news(news_headlines):
    formatted_news = ""
    for article in news_headlines['articles'][:2]:  # Limit to top 3 articles
        title = article['title']
        # description = article['description']
        url = article['url']
        formatted_news += f"<p><strong>{title}</strong></p><p><a href='{url}' target='_blank'>Read more</a></p>"
    return formatted_news.strip()

def news(news_headlines):
    # news_title_list = []
    # news_description_list = []
    # news_url_list = []
    # for i in news_headlines['articles']:
    #     news_title_list.append(i['title'])
    #     news_description_list.append(i['description'])
    #     news_url_list.append(i['url'])
    
    # # getting top 2 news from the response
    # news_title_list = news_title_list[:2]
    # news_description_list = news_description_list[:2]
    # news_url_list = news_url_list[:2]

    # # news_title = random.sample(news_title_list, 2)
    # summary = summarize_news_article(news_title_list, news_description_list, news_url_list)
    # print(summary)
    # message1 = ''
    # for i, j in zip(news_title_list, news_url_list):
    #     print(i)
    #     message1 += i + '\n' + j + '\n'
    return format_news(news_headlines)