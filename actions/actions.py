# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from newsapi import NewsApiClient

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

            # /v2/top-headlines
            sports_headlines = newsapi.get_top_headlines(
                                        language='en',
                                        country='in',
                                        category='sports')

            if sports_headlines['status'] == 'ok':
                dispatcher.utter_message(text=f"Your top headlines is {sports_headlines}")
            else:
                dispatcher.utter_message(text=f"Response not found, Try something else.")

            return []

class ActionIndiaBusinessNews(Action):

    def name(self) -> Text:
        return "action_india_business_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            newsapi = NewsApiClient(api_key='9f090017d52143dc9f8e24f0a56cd505')

            # /v2/top-headlines
            business_headlines = newsapi.get_top_headlines(
                                        language='en',
                                        country='in',
                                        category='business')

            if business_headlines['status'] == 'ok':
                dispatcher.utter_message(text=f"Your top headlines is {business_headlines}")
            else:
                dispatcher.utter_message(text=f"Response not found, Try something else.")

            return []