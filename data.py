import requests

parameters = {
    "amount": 15,
    "type": "boolean",
    "category":18,
}

response = requests.get("https://opentdb.com/api.php", params= parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']



# question_data = [
#     {
#         "category": item['category'],
#         "difficulty": item['difficulty'],
#         "question": item['question'],
#         "correct_answer": item['correct_answer'],
#     } for item in data['results']
# ]
