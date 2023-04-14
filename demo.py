import chat
from chat import ChatGPT
import json
import random

chatbot = chat.ChatGPT()

# a selected example (because gpt originally perform bad in this case)
with open('sharegpt_20230401_clean_lang_split.json', encoding='utf-8') as file:
    data = json.load(file)

formatted_history = ""
for conversation in data:
    if conversation["id"] == "OHGMj1T_0":
        base_index = 0
        history = conversation["conversations"]
        random_integer = 12
        # random_integer = random.randint(base_index, len(history)-base_index-1)
        if history[0]["from"] == "gpt":
            base_index += 1
        for index, chat_detail in enumerate(history):
            string_representation = str(chat_detail)
            if index == random_integer or index == random_integer + 1:
                print(chat_detail)
                if chat_detail["from"] == "gpt":
                    formatted_history+="***"+string_representation+"***"
                else:
                    formatted_history+="!!!"+string_representation+"!!!"
            else:
                formatted_history+=string_representation

print(formatted_history)
chatbot.ask_with_command(formatted_history)