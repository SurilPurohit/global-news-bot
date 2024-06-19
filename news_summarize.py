from openai import OpenAI, APIError, APIConnectionError, OpenAIError
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
import os
# Access the API key for OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
  api_key=openai_api_key,
)

# summarizing news article using gpt 3.5
def summarize_news_article(title, description):
    try:
      prompt=f"Given list of titles and description, formulate a hummanly readable list of news:\n\nList of Titles: {title} \n\nList of Descriptions: {description}"
      response = client.chat.completions.create(
          model="gpt-3.5-turbo-0125",  # You can choose other models like "gpt-3.5-turbo"
          messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
          ],
          max_tokens=350,  # Adjust max_tokens based on the desired summary length
          temperature=0.0,  # Control randomness in the output
      )

      print(response)
      summary = response.choices[0].text.strip()
      return summary

    except OpenAIError as e:
        # Handle API errors
        print(f"OpenAI API error: {e}")
    except Exception as e:
        # Handle other potential errors
        print(f"An error occurred: {e}")
    