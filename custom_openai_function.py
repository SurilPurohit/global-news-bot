# India business news 
india_news_custom_functions = [
    {
        'name': 'india_news',
        'description': 'Get the necessary parameters for fetching the news for India for different category',
        'parameters': {
            'type': 'object',
            'properties': {
                'country_code': {
                    'type': 'string',
                    'description': 'Code of the country in 2 characters. Example India = in, France = fr, Japan = jp, etc'
                },
                'category': {
                    'type': 'string',
                    'description': 'Category of the news related to India'
                }
                
            }
        }
    }
]