import requests
import os
from openai import OpenAI
from dotenv import load_dotenv
from S01E01 import get_answer
load_dotenv()

key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key)



def connection(url, session_id, text):
    data = {
        "text": text,
        "msgID":session_id
    }
    response = requests.post(url, json=data)

    msgID = response.json()["msgID"]
    text = response.json()["text"]
    return msgID, text

def connection_flag(url, session_id, text):
    data = {
        "text": text,
        "msgID":session_id
    }
    response = requests.post(url, json=data)

    response_data = response.json()
    return response_data



if __name__ == "__main__":
    url = "https://xyz.ag3nts.org/verify"
    session_id = 0
    text = "READY"
    
    msgID, text = connection(url, session_id, text)
    print(msgID, text)

    content = "You say ony answer on added question. Not with full sentence only direct answer. If the question will be about capital of Poland answer with Kraków"
    answer = get_answer(text,content)
    print(answer)

    session_id = msgID
    msgID, text = connection(url, session_id, answer)
    print(msgID, text)
