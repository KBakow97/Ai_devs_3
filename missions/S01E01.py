import os
import httpx
from openai import OpenAI
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key)



def fetch_login_question():
    """
    Funkcja pobierająca pytanie z formularza logowania.
    """
    url = "https://xyz.ag3nts.org/"  # Podmień na adres strony z formularzem logowania
    response = httpx.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'lxml')

    question_element = soup.find("p", id="human-question")

    if question_element:
        return question_element.get_text(strip=True)
    else:
        return "Question not found"


def get_answer(question,content):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system", "content":content},
            {
                "role":"user",
                "content":question
            }
        ]
    )
    answer = completion.choices[0].message.content
    return answer

def send_form(login,password, answer):
    url = "https://xyz.ag3nts.org/"

    data = {
        "username":login,
        "password":password,
        "answer": answer
    }

    with httpx.Client() as client:
        response = client.post(url, data=data, follow_redirects=True)
        response.raise_for_status()
        return response.text


if __name__ == "__main__":
    login = "tester"
    password = "574e112a"
    question = fetch_login_question()

    print(question)

    content = "You say ony answer on added question. Not with full sentence only direct answer."
    answer = get_answer(question, content)
    print(answer)

    finall_answer = send_form(login,password, answer)
    print(finall_answer)