import openai
import constants


class ChatGPT():
    def __init__(self):
        openai.api_key = constants.api_key

    def ask(self, system,user,model=4):
        model_name="gpt-3.5-turbo" if model==3.5 else "gpt-4"
        completion = openai.ChatCompletion.create(model=model_name,
                                        messages=self.command(system,user))
        response = completion.choices[0].message["content"]
        print(response)
        return response

    def command(self, system, user):
        return [{"role": "system", "content": system},{"role": "user", "content": user}]
