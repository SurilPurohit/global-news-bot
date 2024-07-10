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
from custom_openai_function import india_news_custom_functions
from news_summarize import summarize_news_article

from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
  api_key=openai_api_key,
)

class ActionIndiaTopHeadlines(Action):

    def name(self) -> Text:
        return "action_india_top_headlines"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            newsapi = NewsApiClient(api_key='9f090017d52143dc9f8e24f0a56cd505')

            # /v2/top-headlines
            top_headlines = newsapi.get_top_headlines(
                                        # q='bitcoin',
                                        # sources='bbc-news,the-verge',
                                        # category='business',
                                        language='en',
                                        country='in')


            dispatcher.utter_message(text=f"Your top headlines is {top_headlines}")

            return []

class ActionIndiaSportsNews(Action):

    def name(self) -> Text:
        return "action_india_sports_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            newsapi = NewsApiClient(api_key='9f090017d52143dc9f8e24f0a56cd505')

            user_message = tracker.latest_message.get('text')

            # extacting the category and country of news from OpenAI library 
            business_news_description = [user_message]
            for i in business_news_description:
                response = client.chat.completions.create(
                    model = 'gpt-3.5-turbo',
                    messages = [{'role': 'user', 'content': i}],
                    functions = india_news_custom_functions,
                    function_call = 'auto'
                )

            # Loading the response as a JSON object
            json_response = json.loads(response.choices[0].message.function_call.arguments)
            json_response = {k.lower(): v for k, v in json_response.items()}
            print(json_response)

            try:
                country_code = json_response['country_code']
                category = json_response['category']
                # /v2/top-sports-headlines
                sports_headlines = newsapi.get_top_headlines(
                                            language='en',
                                            country=country_code,
                                            category=category)

                message = sports_headlines
                # print(message)

                news_title_list = []
                news_description_list = []
                for i in sports_headlines['articles']:
                    news_title_list.append(i['title'])
                    news_description_list.append(i['description'])
                    # news_url_list.append(i['url'])
                
                # getting top 2 sports news from the response
                news_title_list = news_title_list[:8]
                news_description_list = news_description_list[:8]
                # random.sample(test_list, 2)
                summary = summarize_news_article(news_title_list, news_description_list)
                print(summary)
                message1 = ''
                for i in news_title_list:
                    print(i)
                    message1 += i 
                    message1 += '\n'
                
            except:
                message = 'There is a bug in our side, please allow us to fix it.'
                print(message)

            if sports_headlines['status'] == 'ok':
                # dispatcher.utter_message(text=f"Your top headlines is {sports_headlines}")
                dispatcher.utter_message(text=str(f'{message1}'))
            else:
                # dispatcher.utter_message(text=f"Response not found, Try something else.")
                dispatcher.utter_message(text=message)
            return []


class ActionIndiaBusinessNews(Action):

    def name(self) -> Text:
        return "action_india_business_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            # API key for news API
            newsapi = NewsApiClient(api_key='9f090017d52143dc9f8e24f0a56cd505')

            user_message = tracker.latest_message.get('text')

            # extacting the category and country of news from OpenAI library 
            business_news_description = [user_message]
            for i in business_news_description:
                response = client.chat.completions.create(
                    model = 'gpt-3.5-turbo',
                    messages = [{'role': 'user', 'content': i}],
                    functions = india_news_custom_functions,
                    function_call = 'auto'
                )

            # Loading the response as a JSON object
            json_response = json.loads(response.choices[0].message.function_call.arguments)
            json_response = {k.lower(): v for k, v in json_response.items()}
            print(json_response)

            try:
                country_code = json_response['country_code']
                category = json_response['category']
                # /v2/top-business-headlines
                business_headlines = newsapi.get_top_headlines(
                                            language='en',
                                            country=country_code,
                                            category=category)

                message = business_headlines
                # print(message)

                news_title_list = []
                news_description_list = []
                for i in business_headlines['articles']:
                    news_title_list.append(i['title'])
                    news_description_list.append(i['description'])
                
                # getting top 2 business news from the response
                news_title_list = news_title_list[:8]
                news_description_list = news_description_list[:8]
                summary = summarize_news_article(news_title_list, news_description_list)
                print(summary)
                message1 = ''
                for i in news_title_list:
                    print(i)
                    message1 += i 
                    message1 += '\n\n'

            except:
                message = 'There is a bug in our side, please allow us to fix it.'
                print(message)

            if business_headlines['status'] == 'ok':
                # dispatcher.utter_message(text=f"Your top headlines is {business_headlines}")
                dispatcher.utter_message(text=str(f'{message1}'))
                
            else:
                # dispatcher.utter_message(text=f"Response not found, Try something else.")
                dispatcher.utter_message(text=message)

            return []