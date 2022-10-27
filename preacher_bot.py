from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_sequence = "\nPreacher:"
restart_sequence = "\n\nMe:"
session_prompt = " Your man of God message here "

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
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

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
