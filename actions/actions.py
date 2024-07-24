# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from newsapi import NewsApiClient

import os
from openai import OpenAI

import json
from custom_openai_function import news_custom_functions
from custom_openai_topnews import topnews_custom_functions
from news_summarize import summarize_news_article
from utils import news
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
news_api = os.getenv('NEWS_API')

client = OpenAI(
  api_key=openai_api_key
)

class ActionIndiaTopHeadlines(Action):

    def name(self) -> Text:
        return "action_india_top_headlines"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            newsapi = NewsApiClient(api_key=news_api)

            user_message = tracker.latest_message.get('text')
            user_message = user_message.lower()
            print(f'User Message: {user_message}')
            # extacting the category and country of news from OpenAI library 
            try:
                news_description = [user_message]
                for i in news_description:
                    response = client.chat.completions.create(
                        model = 'gpt-3.5-turbo',
                        messages = [{'role': 'user', 'content': i}],
                        functions = topnews_custom_functions,
                        function_call = 'auto'
                    )

                # Loading the response as a JSON object
                json_response = json.loads(response.choices[0].message.function_call.arguments)
                json_response = {k.lower(): v for k, v in json_response.items()}
                print(f'Top News OpenAI output: {json_response}')
            
                print('Country Code', json_response['country_code'])
                country_code = json_response['country_code']
                print('code:', country_code)
                # category = json_response['category']
                # /v2/top-news-headlines
                news_headlines = newsapi.get_top_headlines(
                                            language='en',
                                            country=country_code)

                message = news_headlines
                print(message)

                message1 = news(news_headlines)

            except:
                news_headlines = newsapi.get_top_headlines(
                                        language='en',
                                        country='in')
                
                message1 = news(news_headlines)

            if news_headlines['status'] == 'ok':
                # dispatcher.utter_message(text=f"Your top headlines is {sports_headlines}")
                dispatcher.utter_message(text=str(f'{message1}'))
            else:
                # dispatcher.utter_message(text=f"Response not found, Try something else.")
                dispatcher.utter_message(text='There is a bug on our side and we are working on it.')
            return []

class ActionIndiaSportsNews(Action):

    def name(self) -> Text:
        return "action_india_sports_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            newsapi = NewsApiClient(api_key=news_api)

            user_message = tracker.latest_message.get('text')
            user_message = user_message.lower()
            print(f'User Message: {user_message}')

            # extacting the category and country of news from OpenAI library 
            try:
                business_news_description = [user_message]
                for i in business_news_description:
                    response = client.chat.completions.create(
                        model = 'gpt-3.5-turbo',
                        messages = [{'role': 'user', 'content': i}],
                        functions = news_custom_functions,
                        function_call = 'auto'
                    )

                # Loading the response as a JSON object
                json_response = json.loads(response.choices[0].message.function_call.arguments)
                json_response = {k.lower(): v for k, v in json_response.items()}
                print(json_response)

            
                country_code = json_response['country_code']
                category = json_response['category']
                
                print('Country Code', json_response['country_code'])
                print('code:', country_code, 'category: ', category)
                # /v2/top-sports-headlines
                sports_headlines = newsapi.get_top_headlines(
                                            language='en',
                                            country=country_code,
                                            category=category)

                message1 = news(sports_headlines)
                
            except:
                sports_headlines = newsapi.get_top_headlines(
                                        language='en',
                                        country='in',
                                        category='sports')
                
                message1 = news(sports_headlines)

            if sports_headlines['status'] == 'ok':
                # dispatcher.utter_message(text=f"Your top headlines is {sports_headlines}")
                dispatcher.utter_message(text=str(f'{message1}'))
            else:
                # dispatcher.utter_message(text=f"Response not found, Try something else.")
                dispatcher.utter_message(text='There is a bug on our side and we are working on it.')
            return []


class ActionIndiaBusinessNews(Action):

    def name(self) -> Text:
        return "action_india_business_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            # API key for news API
            newsapi = NewsApiClient(api_key=news_api)

            user_message = tracker.latest_message.get('text')
            user_message = user_message.lower()
            print(f'User Message: {user_message}')

            # extacting the category and country of news from OpenAI library 
            business_news_description = [user_message]
            for i in business_news_description:
                response = client.chat.completions.create(
                    model = 'gpt-3.5-turbo',
                    messages = [{'role': 'user', 'content': i}],
                    functions = news_custom_functions,
                    function_call = 'auto'
                )

            # Loading the response as a JSON object
            json_response = json.loads(response.choices[0].message.function_call.arguments)
            json_response = {k.lower(): v for k, v in json_response.items()}
            print(json_response)

            try:
                country_code = json_response['country_code']
                category = json_response['category']
                print('Country Code', json_response['country_code'])
                print('code:', country_code, 'category: ', category)
                # /v2/top-business-headlines
                business_headlines = newsapi.get_top_headlines(
                                            language='en',
                                            country=country_code,
                                            category=category)

                message1 = news(business_headlines)

            except:
                business_headlines = newsapi.get_top_headlines(
                                        language='en',
                                        # country='in',
                                        category='business')
                
                message1 = news(business_headlines)

            if business_headlines['status'] == 'ok':
                # dispatcher.utter_message(text=f"Your top headlines is {business_headlines}")
                dispatcher.utter_message(text=str(f'{message1}'))
            else:
                # dispatcher.utter_message(text=f"Response not found, Try something else.")
                dispatcher.utter_message(text='There is a bug on our side and we are working on it.')

            return []