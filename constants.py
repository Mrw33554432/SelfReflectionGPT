command = """Please response following these rules:
1. The selected request is bounded with !!!request!!!. Copy the selected request unchanged, start with <<start request>>, end with <<end request>>.
2. You should analyze the intuition(why) of the response based on the given past conversation (consider the previous and following conversation), start with <<start analyze>>,end with <<end analyze>>.
3. The selected response is bounded with ***response***. Write a better response with the given context. The new reply should be provided to replace the string bounded with ***response***. New response should start with <<new reply>> end with <<end reply>>.
4. You should consider chats after the selected message as a feedback.
Here is the conversation:"""

api_key = ""
