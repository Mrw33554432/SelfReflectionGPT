import chat
from chat import ChatGPT
import json
import random
from CommandGenerator import CommandGenerator

chatbot = chat.ChatGPT()

# a selected example (because gpt originally perform bad in this case)
with open('sharegpt_20230401_clean_lang_split.json', encoding='utf-8') as file:
    data = json.load(file)

formatted_history = ""
for conversation in data:
    if conversation["id"] == "skuuYph_0":
        base_index = 0
        history = conversation["conversations"]
        random_integer = 0
        # random_integer = random.randint(base_index, len(history)-base_index-1) # or you can iterate through every chat
        if history[0]["from"] == "gpt":
            base_index += 1
        for index, chat_detail in enumerate(history):
            if chat_detail["from"] == "human":
                role="Q"
            else:
                role="A"
            string_representation = role + ":" + str(chat_detail["value"])+"\n"
            if index == random_integer:
                print("start")
                formatted_history+="K"+string_representation[1:]
            elif index == random_integer + 1:
                print("end")
                formatted_history+="L"+string_representation[1:]
            else:
                formatted_history+=string_representation

print(formatted_history)
generator=CommandGenerator(formatted_history)
command=generator.generate_command()
input=generator.generate_input()
print(command)
chatbot.ask(command,input)