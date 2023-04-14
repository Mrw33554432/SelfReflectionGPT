# Generating Meaningful Training Data from Chat for Self-Evolving Large Language Models

![WorkFlow graph](graph_0.png)
## Introduction

Large language models, like GPT, have transformed natural language processing by achieving unparalleled results in a variety of NLP tasks. However, they still need an extensive amount of high-quality training data for optimal performance. In this project, we propose an innovative method for generating meaningful training data from chat interactions, enabling large language models to become self-evolving.

### core advantage
1. With this approach, we can generate a dataset of high quality conversation/response not just better than native GPT-4, but also better than human level in many cases (because the model already know what is going to happen in the future when making response - we give it to the model).


2. The methodology proposed in this essay for generating training data from chat interactions and enabling self-evolution of large language models has the potential to push these models even further. It is worth noting that OpenAI does not store conversation history data on their end. As a result, it is reasonable to assume that they did not use a method similar to the one proposed here in their model training. This suggests that our approach could indeed offer a novel and promising direction for enhancing the capabilities of large language models.


3. It can be used for improve the data quality for all kinds of data, including human-human/human-AI/AI-human/AI-AI conversations.
## Methodology

Our approach harnesses the power of interactive chat to create high-quality training data. By enabling users to converse with a language model, we can gather a substantial amount of diverse, context-rich data that can be employed for fine-tuning the model.

However, using chat data without further modification is not an ideal approach. To address this, we have designed a method that allows the model to produce improved responses from subsequent conversations. Then, we can use the enhanced response along with the previous conversation as training data, enabling the model to respond more effectively. Ideally, this method should help the model comprehend implicit meanings in a conversation.

This approach not only generates training data, but it also allows the model to continuously evolve and improve through interactions with more users.




## Results

Our method has demonstrated promising results in producing high-quality response/training data. Obviously with the high quality training date generated with the method, we can enhance the performance of large language models. 

Moreover, our self-evolving approach allows the model to continuously improve as it interacts with more users and generates additional training data. This has the potential to result in significant advancements in the overall performance of large language models.

## Conclusion

In summary, our method introduces a new and innovative approach for generating meaningful training data for large language models and making them self-evolving. By capitalizing on the power of interactive chat, we can generate high-quality training data and consistently improve the performance of these models. This has the potential to significantly advance the field of NLP and bring us closer to achieving human-like language understanding in AI.



## Example
### Direct input
<details>
  <summary>Click to expand</summary>
  
you can directly copy the text and paste it into GPT-4 webchat

input:
```markdown
Please response following these rules:
1. The selected request is bounded with !!!request!!!. Copy the selected request unchanged, start with <<start request>>, end with <<end request>>.
2. You should analyze the intuition(why) of the response based on the given past conversation (consider the previous and following conversation), start with <<start analyze>>,end with <<end analyze>>.
3. The selected response is bounded with ***response***. Write a better response with the given context. The new reply should be provided to replace the string bounded with ***response***. New response should start with <<new reply>> end with <<end reply>>.
4. You should consider chats after the selected message as a feedback.
Here is the conversation:
{
    "id": "OHGMj1T_0",
    "conversations": [
      {
        "from": "human",
        "value": "Who sings the italo disco song \"sonambulismo\"?"
      },
      {
        "from": "gpt",
        "value": "The Italo Disco song \"Sonambulismo\" is performed by the Italian musician and singer Pino D'Angi\u00f2. The song was released in 1984 and became a hit in Italy and other European countries."
      },
      {
        "from": "human",
        "value": "give me the lyrics"
      },
      {
        "from": "gpt",
        "value": "Certainly, here are the lyrics to \"Sonambulismo\" by Pino D'Angi\u00f2:\n\nVerse 1:\nC'\u00e8 un'ombra nella notte\nChe mi segue sempre pi\u00f9\n\u00c8 una voce che mi chiama\nChe mi vuole un po' di pi\u00f9\n\nChorus:\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\n\nVerse 2:\nNon mi posso svegliare\nNon riesco a non sognare\nSento il vento sulla pelle\nMa non so dove andare\n\nChorus:\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\n\nVerse 3:\nVivo come in un film\nDove il tempo non esiste\nFaccio tutto quello che voglio\nMa non mi sento felice\n\nChorus:\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\n\nVerse 4:\nC'\u00e8 una porta che mi chiama\nMa non so dove conduce\nNon so se devo entrare\nO continuare a sognare\n\nChorus:\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito"
      },
      {
        "from": "human",
        "value": "Who sings the Italo Disco song \"Sonnambulismo\"?"
      },
      {
        "from": "gpt",
        "value": "The Italo Disco song \"Sonnambulismo\" is performed by Pino D'Angi\u00f2, an Italian musician and singer. The song was released in 1984 and became a hit in Italy and other European countries."
      },
      {
        "from": "human",
        "value": "I mean the song by Canton"
      },
      {
        "from": "gpt",
        "value": "I apologize for the confusion earlier. The Italo Disco song \"Sonnambulismo\" you are referring to is actually performed by the Italian singer and producer Canton. The song was released in 1986 and became a popular hit in Italy and other parts of Europe. Here are the lyrics:\n\nVerse 1:\nC'\u00e8 una casa bianca\ndove io mi sento in pace\ntutto intorno il silenzio\ne la notte su di me\n\nChorus:\nSonnambulismo\ncammino in sogno solo\nnon ho un'et\u00e0\nnon ho un'identit\u00e0\n\nVerse 2:\nVedo tante cose\nche non so se sono vere\ne cammino piano\nsenza sapere dove andr\u00f2\n\nChorus:\nSonnambulismo\ncammino in sogno solo\nnon ho un'et\u00e0\nnon ho un'identit\u00e0\n\nBridge:\nMa poi mi sveglio e guardo\nil mio viso nella luce\ne sento una nostalgia\nche non so spiegare\n\nChorus:\nSonnambulismo\ncammino in sogno solo\nnon ho un'et\u00e0\nnon ho un'identit\u00e0"
      },
      {
        "from": "human",
        "value": "That's not the lyrics, it starts with \"Buonanotte a tutti voi\""
      },
      {
        "from": "gpt",
        "value": "I apologize for the mistake in my previous response. You are correct, \"Sonnambulismo\" is a different song by Canton, and the lyrics begin with \"Buonanotte a tutti voi.\" Here are the correct lyrics to the song:\n\nVerse 1:\nBuonanotte a tutti voi\n\u00c8 l'ora di dormire ormai\nE io mi sento un po' diverso\nCammino piano e non so dove andr\u00f2\n\nChorus:\nSonnambulismo, sonnambulismo\nLa mia vita \u00e8 un sogno infinito\nSonnambulismo, sonnambulismo\nNon so pi\u00f9 cosa sia la realt\u00e0\n\nVerse 2:\nI colori sono sfocati\nE le luci sembrano ovattate\nSento solo il rumore del mio respiro\nE questo sogno che non ha fine\n\nChorus:\nSonnambulismo, sonnambulismo\nLa mia vita \u00e8 un sogno infinito\nSonnambulismo, sonnambulismo\nNon so pi\u00f9 cosa sia la realt\u00e0\n\nBridge:\nSono solo un sonnambulo\nChe cammina senza meta\nNon so se voglio svegliarmi\nO continuare a sognare\n\nChorus:\nSonnambulismo, sonnambulismo\nLa mia vita \u00e8 un sogno infinito\nSonnambulismo, sonnambulismo\nNon so pi\u00f9 cosa sia la realt\u00e0\n\nOutro:\nLa mia vita \u00e8 un sogno infinito."
      },
      {
        "from": "human",
        "value": "Here's the song's chorus:\n\nSonnambulismo \u00e8 una parola\nche vi meraviglier\u00e0,\nma quante cose questa notte\nstrana mi riveler\u00e0,\nsonnambulismo \u00e8 il desiderio\ndi sfuggire ad un clich\u00e9,\nsereno, allegro, malinconico\ncammino senza te."
      },
      {
        "from": "gpt",
        "value": "I apologize again for the confusion earlier. You are correct that the Italo Disco song \"Sonnambulismo\" you were asking about has lyrics that are different from the two sets I provided earlier. Here are the correct lyrics to the song by Gazebo:\n\nVerse 1:\nBuonanotte a tutti voi\nE' l'ora di dormire ormai\nMa io mi sento un po' diverso\nCammino piano e non so dove andr\u00f2\n\nChorus:\nSonnambulismo \u00e8 una parola\nChe vi meraviglier\u00e0\nMa quante cose questa notte\nStrana mi riveler\u00e0\nSonnambulismo \u00e8 il desiderio\nDi sfuggire ad un clich\u00e9\nSereno, allegro, malinconico\nCammino senza te\n\nVerse 2:\nNon so se \u00e8 un sogno o realt\u00e0\nQuesta vita che sto vivendo qua\nMa qualcosa di strano c'\u00e8\nE questa notte mi stupir\u00e0\n\nChorus:\nSonnambulismo \u00e8 una parola\nChe vi meraviglier\u00e0\nMa quante cose questa notte\nStrana mi riveler\u00e0\nSonnambulismo \u00e8 il desiderio\nDi sfuggire ad un clich\u00e9\nSereno, allegro, malinconico\nCammino senza te\n\nBridge:\nE mi sembra di volare via\nIn un mondo che non c'\u00e8\nMa poi mi sveglio e guardo\nLa mia vita nella luce\n\nChorus:\nSonnambulismo \u00e8 una parola\nChe vi meraviglier\u00e0\nMa quante cose questa notte\nStrana mi riveler\u00e0\nSonnambulismo \u00e8 il desiderio\nDi sfuggire ad un clich\u00e9\nSereno, allegro, malinconico\nCammino senza te\n\nOutro:\nSonnambulismo \u00e8 il desiderio\nDi sfuggire ad un clich\u00e9\nSereno, allegro, malinconico\nCammino senza te."
      },
!!!      {
        "from": "human",
        "value": "Can you make a non-sensical portuguese version of the chorus that keeps the same rhythm and syllable structure?"
      }!!!,
***      {
        "from": "gpt",
        "value": "Certainly, here's a non-sensical Portuguese version of the chorus with the same syllable structure and rhythm:\n\nSonambulismo \u00e9 uma palavra\nQue vai te surpreender\nQuantas coisas essa noite louca\nVai me fazer entender\nSonambulismo \u00e9 o desejo\nDe escapar de um clich\u00ea\nSereno, alegre, melanc\u00f3lico\nCaminho sem voc\u00ea"
      }***,
      {
        "from": "human",
        "value": "You don't need to keep the same meaning, actually you should change it to make less sense. Just keep around the word \"Sonambulismo\" and the same syllable count."
      },
      {
        "from": "gpt",
        "value": "I apologize for the misunderstanding. Here's a non-sensical Portuguese version of the chorus with the same syllable count and keeping the word \"Sonambulismo\":\n\nSonambulismo \u00e9 uma palavra\nQue vai te fazer rir\nQuantas coisas essa noite maluca\nVai me fazer sentir\nSonambulismo \u00e9 o desejo\nDe voar sem um porqu\u00ea\nSereno, alegre, melanc\u00f3lico\nCaminho sem voc\u00ea"
      },
      {
        "from": "human",
        "value": "You can replace the \"definition\" of Sonambulismo in the first and fifth lines for random unrelated words with the same syllable count"
      },
      {
        "from": "gpt",
        "value": "Thank you for the clarification. Here's a version with random unrelated words:\n\nMonossilabismo \u00e9 uma cenoura\nQue vai te iluminar\nQuantas coisas essa noite cavalga\nVai me fazer cantar\nPolilogismo \u00e9 o desejo\nDe pintar sem um pincel\nSereno, alegre, melanc\u00f3lico\nCaminho sem papel"
      }
    ]
  }
```
Response:
```markdown
<<start analyze>>The user asked for a non-sensical Portuguese version of the chorus that keeps the same rhythm and syllable structure, and I provided a version that still made sense. The user then specified that they wanted to change the meaning of the lines to make less sense, only keeping the word "Sonambulismo" and the same syllable count.<<end analyze>>

<<start request>>Can you make a non-sensical portuguese version of the chorus that keeps the same rhythm and syllable structure?<<end request>>

<<new reply>>Understood. Here's a non-sensical Portuguese version of the chorus with the same syllable count and keeping the word "Sonambulismo":

Sonambulismo abacaxi
Mangueira vai desabar
Quantas frutas essa noite girafa
Vai me fazer engolir
Sonambulismo liquidificador
De dançar sem um chapéu
Sereno, alegre, melancólico
Caminho sem anzol<<end reply>>
```
</details>

### OpenAI api request
<details>
  <summary>Click to expand</summary>

[You can find the dataset here](https://huggingface.co/datasets/philschmid/sharegpt-raw/blob/main/sharegpt_20230401_clean_lang_split.json)

  code:

```python
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
```
Response:
```python
"""
<<start request>>Can you make a non-sensical portuguese version of the chorus that keeps the same rhythm and syllable structure?<<end request>> <<start analyze>>The user is requesting a non-sensical version of the chorus in Portuguese that maintains the same rhythm and syllable structure. Previous replies provided by the AI were still somewhat coherent in terms of meaning.<<end analyze>> <<new reply>>Considerando o pedido, aqui está uma versão do refrão em português sem sentido lógico, mantendo a palavra "Sonambulismo" e a mesma quantidade de sílabas:

Sonambulismo, laranja azul
Mistura abacaxi, lampião
Bagunçando noite, vento carrossel
Capivara alado, serpente colchão
Sonambulismo, celular de sal
Dança ilhabela, borboleta cão
Amendoim, risonho, abacate triste
Sem caranguejo, caminho croissant
<<end reply>>
"""
```
</details>


### Training Data
<details>
  <summary>Click to expand</summary>
This is just a simple example, you can modify it as you want

example:

  ```python
{
    "history":
        """
            [{
                "from": "human",
                "value": "Who sings the italo disco song \"sonambulismo\"?"
              },
              {
                "from": "gpt",
                "value": "The Italo Disco song \"Sonambulismo\" is performed by the Italian musician and singer Pino D'Angi\u00f2. The song was released in 1984 and became a hit in Italy and other European countries."
              },
              {
                "from": "human",
                "value": "give me the lyrics"
              },
              {
                "from": "gpt",
                "value": "Certainly, here are the lyrics to \"Sonambulismo\" by Pino D'Angi\u00f2:\n\nVerse 1:\nC'\u00e8 un'ombra nella notte\nChe mi segue sempre pi\u00f9\n\u00c8 una voce che mi chiama\nChe mi vuole un po' di pi\u00f9\n\nChorus:\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\n\nVerse 2:\nNon mi posso svegliare\nNon riesco a non sognare\nSento il vento sulla pelle\nMa non so dove andare\n\nChorus:\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\n\nVerse 3:\nVivo come in un film\nDove il tempo non esiste\nFaccio tutto quello che voglio\nMa non mi sento felice\n\nChorus:\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\n\nVerse 4:\nC'\u00e8 una porta che mi chiama\nMa non so dove conduce\nNon so se devo entrare\nO continuare a sognare\n\nChorus:\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito\nSonambulismo, sonambulismo\nLa mia vita \u00e8 un sonno, un sogno infinito"
              },
              {
                "from": "human",
                "value": "Who sings the Italo Disco song \"Sonnambulismo\"?"
              },
              {
                "from": "gpt",
                "value": "The Italo Disco song \"Sonnambulismo\" is performed by Pino D'Angi\u00f2, an Italian musician and singer. The song was released in 1984 and became a hit in Italy and other European countries."
              },
              {
                "from": "human",
                "value": "I mean the song by Canton"
              },
              {
                "from": "gpt",
                "value": "I apologize for the confusion earlier. The Italo Disco song \"Sonnambulismo\" you are referring to is actually performed by the Italian singer and producer Canton. The song was released in 1986 and became a popular hit in Italy and other parts of Europe. Here are the lyrics:\n\nVerse 1:\nC'\u00e8 una casa bianca\ndove io mi sento in pace\ntutto intorno il silenzio\ne la notte su di me\n\nChorus:\nSonnambulismo\ncammino in sogno solo\nnon ho un'et\u00e0\nnon ho un'identit\u00e0\n\nVerse 2:\nVedo tante cose\nche non so se sono vere\ne cammino piano\nsenza sapere dove andr\u00f2\n\nChorus:\nSonnambulismo\ncammino in sogno solo\nnon ho un'et\u00e0\nnon ho un'identit\u00e0\n\nBridge:\nMa poi mi sveglio e guardo\nil mio viso nella luce\ne sento una nostalgia\nche non so spiegare\n\nChorus:\nSonnambulismo\ncammino in sogno solo\nnon ho un'et\u00e0\nnon ho un'identit\u00e0"
              },
              {
                "from": "human",
                "value": "That's not the lyrics, it starts with \"Buonanotte a tutti voi\""
              },
              {
                "from": "gpt",
                "value": "I apologize for the mistake in my previous response. You are correct, \"Sonnambulismo\" is a different song by Canton, and the lyrics begin with \"Buonanotte a tutti voi.\" Here are the correct lyrics to the song:\n\nVerse 1:\nBuonanotte a tutti voi\n\u00c8 l'ora di dormire ormai\nE io mi sento un po' diverso\nCammino piano e non so dove andr\u00f2\n\nChorus:\nSonnambulismo, sonnambulismo\nLa mia vita \u00e8 un sogno infinito\nSonnambulismo, sonnambulismo\nNon so pi\u00f9 cosa sia la realt\u00e0\n\nVerse 2:\nI colori sono sfocati\nE le luci sembrano ovattate\nSento solo il rumore del mio respiro\nE questo sogno che non ha fine\n\nChorus:\nSonnambulismo, sonnambulismo\nLa mia vita \u00e8 un sogno infinito\nSonnambulismo, sonnambulismo\nNon so pi\u00f9 cosa sia la realt\u00e0\n\nBridge:\nSono solo un sonnambulo\nChe cammina senza meta\nNon so se voglio svegliarmi\nO continuare a sognare\n\nChorus:\nSonnambulismo, sonnambulismo\nLa mia vita \u00e8 un sogno infinito\nSonnambulismo, sonnambulismo\nNon so pi\u00f9 cosa sia la realt\u00e0\n\nOutro:\nLa mia vita \u00e8 un sogno infinito."
              },
              {
                "from": "human",
                "value": "Here's the song's chorus:\n\nSonnambulismo \u00e8 una parola\nche vi meraviglier\u00e0,\nma quante cose questa notte\nstrana mi riveler\u00e0,\nsonnambulismo \u00e8 il desiderio\ndi sfuggire ad un clich\u00e9,\nsereno, allegro, malinconico\ncammino senza te."
              },
              {
                "from": "gpt",
                "value": "I apologize again for the confusion earlier. You are correct that the Italo Disco song \"Sonnambulismo\" you were asking about has lyrics that are different from the two sets I provided earlier. Here are the correct lyrics to the song by Gazebo:\n\nVerse 1:\nBuonanotte a tutti voi\nE' l'ora di dormire ormai\nMa io mi sento un po' diverso\nCammino piano e non so dove andr\u00f2\n\nChorus:\nSonnambulismo \u00e8 una parola\nChe vi meraviglier\u00e0\nMa quante cose questa notte\nStrana mi riveler\u00e0\nSonnambulismo \u00e8 il desiderio\nDi sfuggire ad un clich\u00e9\nSereno, allegro, malinconico\nCammino senza te\n\nVerse 2:\nNon so se \u00e8 un sogno o realt\u00e0\nQuesta vita che sto vivendo qua\nMa qualcosa di strano c'\u00e8\nE questa notte mi stupir\u00e0\n\nChorus:\nSonnambulismo \u00e8 una parola\nChe vi meraviglier\u00e0\nMa quante cose questa notte\nStrana mi riveler\u00e0\nSonnambulismo \u00e8 il desiderio\nDi sfuggire ad un clich\u00e9\nSereno, allegro, malinconico\nCammino senza te\n\nBridge:\nE mi sembra di volare via\nIn un mondo che non c'\u00e8\nMa poi mi sveglio e guardo\nLa mia vita nella luce\n\nChorus:\nSonnambulismo \u00e8 una parola\nChe vi meraviglier\u00e0\nMa quante cose questa notte\nStrana mi riveler\u00e0\nSonnambulismo \u00e8 il desiderio\nDi sfuggire ad un clich\u00e9\nSereno, allegro, malinconico\nCammino senza te\n\nOutro:\nSonnambulismo \u00e8 il desiderio\nDi sfuggire ad un clich\u00e9\nSereno, allegro, malinconico\nCammino senza te."
              }]
          """,
    "input":
        "Can you make a non-sensical portuguese version of the chorus that keeps the same rhythm and syllable structure?",
    "output":
        """
        Understood. Here's a non-sensical Portuguese version of the chorus with the same syllable count and keeping the word "Sonambulismo":\n\nSonambulismo abacaxi\nMangueira vai desabar\nQuantas frutas essa noite girafa\nVai me fazer engolir\nSonambulismo liquidificador\nDe dançar sem um chapéu\nSereno, alegre, melancólico\nCaminho sem anzol"""}
```
</details>

## WIPs
1. Generate a dataset
2. Validate the quality of response in statistical data (even though it's obviously better)
3. Using data this method on fine-tuning an open-source LLM
4. Publish the LLM for public access, and use the public chat data for further model updates (this is why it is called self evolve)