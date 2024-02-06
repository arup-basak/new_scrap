import os

import google.generativeai as gen_ai
import re
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
model = gen_ai.GenerativeModel('gemini-pro')
gen_ai.configure(api_key=GOOGLE_API_KEY)

def convert_into_array(inputStr):
    return [re.sub(r'\d+\.\s*', '', line) for line in inputStr.split("\n") if re.match(r'\d+\.\s*', line)]


def get_topics(area):
    response = model.generate_content(
        contents=f"Give me 5 best news keywords to get news of Riots, Election, Festival Violence or Communal "
                 f"Violence in {area}"
    )
    response_array = convert_into_array(response.text)
    return response_array
