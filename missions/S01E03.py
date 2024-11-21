import json
import re
import requests
from S01E01 import get_answer

with open("kalibracja.json", "r") as file:
    data = json.load(file)

data["apikey"] = "77e0c508-1a1f-4d06-9060-e6034fdac101"
content = "You say only answer on added question. Not with full sentence only direct answer."

for item in data['test-data']:
    question = item["question"]
    answer = item["answer"]
    if 'test' in item:
        q = item['test']["q"]
        ans = get_answer(q,content)
        item['test']["a"] = ans

    numbers = re.findall(r'\d+', question)
    suma = int(numbers[0]) + int(numbers[1])
    if suma != answer:

        item["answer"] = suma

url = "https://centrala.ag3nts.org/report"
headers = {
    "Content-Type": "application/json",
}

task_name = "JSON"


data_to_send = {
    "task": task_name,
    "apikey": data["apikey"],
    "answer": data
}
response = requests.post(url, headers=headers, json=data_to_send)
print(response.json())
