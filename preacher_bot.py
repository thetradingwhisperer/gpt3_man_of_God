#%%
from dotenv import load_dotenv
import os
import openai

#%%
load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
#%%
start_sequence = "\nPreacher:"
restart_sequence = "\nMe: "
session_prompt = "The following is a conversation with an AI pastor. The pastor is helpful, gives words of biblical knowledge and understand based on the word of God in the Bible.\n\nPreacher: Hello there. How can I help you?\n\nMe: I was wondering if you could tell me a little bit about the Bible.\n\nPreacher: Sure! The Bible is the word of God, and it is our guide for living. It contains everything we need to know about God and how to live a godly life."

def ask(question):
    prompt_text = f'{session_prompt}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt_text,
    temperature=0.9,
    max_tokens=923,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["\n"]
    )
    story = response['choices'][0]['text']
    return str(story)
