from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
import os
# Access the API key
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
  api_key=openai_api_key,
)

def summarize_news_article(title, description):
    response = client.chat.completions.create(
        engine="gpt-3.5-turbo-0125",  # You can choose other models like "gpt-3.5-turbo"
        prompt=f"Given list of titles and description, formulate a hummanly readable list of news:\n\nList of Titles: {title} \n\nList of Descriptions: {description}",
        max_tokens=350,  # Adjust max_tokens based on the desired summary length
        temperature=0.0,  # Control randomness in the output
    )
    print('news_summarize')
    summary = response.choices[0].text.strip()
    return summary