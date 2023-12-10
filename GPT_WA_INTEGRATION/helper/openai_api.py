import os

from openai import OpenAI
import openai
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
client = OpenAI()


def text_complition(prompt: str) -> dict:
    '''
    Call Openai API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict
    '''

    try:
        system_prompt = "You are a helpful assistant"
        response = client.chat.completions.create( # Change the method name
                   model = 'gpt-3.5-turbo',
                   messages = [ # Change the prompt parameter to messages parameter
                    {"role": "system", "content": system_prompt}, 
                    {"role": "user", "content": prompt}
                    ],
                   temperature = 0 
                 )
        return {
            'status': 1,
            'response': response.choices[0].message.content
        }
    except:
        return {
            'status': 0,
            'response': 'Some Error has occured'
        }
