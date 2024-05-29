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
