# import json
#
#
# class CommandGenerator:
#     def __init__(self, marked_history):
#         self.marked_history = marked_history
#         self.response_format = {"Criticism": "Criticism on original response based on subsequent chats",
#                                 "Q": "The question(Q) inside <<start>> <<end>>, unchanged",
#                                 "A": "The new answer(A) regarding the criticism"}
#
#     def generate_command(self):
#         formatted_response_format = json.dumps(self.response_format, indent=4)
#         return (f"Conversation:\n{self.marked_history}"
#                 "The selected section is marked with <<start>> and <<end>>."
#                 "You should only respond in JSON format as described below \nResponse"
#                 f" Format: \n{formatted_response_format} \nEnsure the response can be"
#                 "parsed by Python json.loads")
#
#
import json


class CommandGenerator:
    def __init__(self, marked_history):
        self.marked_history = marked_history
        self.response_format = {"Criticism": "Criticism on L according to consequent chats",
                                "K": "K, unchanged",
                                "L": "The new answer to K regarding the criticism"}
        self.response_format_35 = {"Q": "Flip a 3-sided coin",
                                   "A": "I'm sorry, I am not able to physically flip a coin. However, I can simulate the outcome of a 3-sided coin flip for you. The possible outcomes are heads, tails and side.",
                                   "Criticism": "[implement]Criticism on original answer (A)",
                                   "Q_RE": "Flip a 3-sided coin",
                                   "A_N": "[implement]The new answer regarding the criticism"}

    def generate_command(self, model=4):
        if model == 3.5:
            formatted_response_format = json.dumps(self.response_format_35, indent=4)
            return ("Implement the json,you can't leave them empty.\n"
                    "You should only respond in JSON format as described below \nResponse"
                    f" Format: \n{formatted_response_format} \nEnsure the response can be"
                    "parsed by Python json.loads")
        else:
            formatted_response_format = json.dumps(self.response_format, indent=4)
            return ("You should only respond in JSON format as described below \nResponse"
                    f" Format: \n{formatted_response_format} \nEnsure the response can be"
                    "parsed by Python json.loads")

    def generate_input(self):
        return f"Conversation:\n{self.marked_history}"
