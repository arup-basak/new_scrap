import google.generativeai as gen_ai
from summarize import get_summarize_text
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = gen_ai.GenerativeModel('gemini-pro')
gen_ai.configure(api_key=GOOGLE_API_KEY)


def get_sentiment(content):
    response = model.generate_content(
        contents=f"I have the scrapped body, give me the sentiment analysis at the scale of 100, 0 means no violence "
                 f"and 75+ means theres a chance of violence, the content is '{get_summarize_text(content)}'"
    )
    return response.text
