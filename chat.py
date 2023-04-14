import openai
import constants


class ChatGPT():
    def __init__(self):
        openai.api_key = constants.api_key

    def ask_with_command(self, history):
        completion = openai.ChatCompletion.create(model="gpt-4",
                                        messages=self.command(history))
        response = completion.choices[0].message["content"]
        print(response)
        return response

    def command(self, history):
        return [{"role": "system", "content": constants.command},{"role": "user", "content": history}]
