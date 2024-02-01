import json
from openai import OpenAI

INITIAL_PERSONA_PROMPT = "You are a helpful assistant designed to output JSON. You will impersonate a persona to help me answer a few form questions. You will give answers from the view of a 25 year old male, living on his onw in an urban city. The persona's parents are divorced recently., but had a very abusive attitude to one another and to your persona for more than 10 years now. Remember to give the answer in JSON format with the property answer beeing the answer."

class AnswerBot():
    def __init__(self, api_key, initial_prompt):
        self.api_key = api_key
        self.initial_prompt = " ".join(initial_prompt)
        self.min_answer = 1
        self.max_answer = 5
        self.min_meaning = "never"
        self.max_meaning = "very often"
        self.messages=[
                {"role": "system", "content": self.initial_prompt},
            ]
        global client
        client = OpenAI(api_key=api_key)


    def set_limits(self, min_answer, min_meaning, max_answer, max_meaning):
        self.min_answer = min_answer
        self.max_answer = max_answer
        self.min_meaning = min_meaning
        self.max_meaning = max_meaning


    def answer(self, question_text):
        self.messages.append(                
            {"role": "user", "content": f"Raspunde cu un numar intre {self.min_answer} (adica {self.min_meaning}) si {self.max_answer} (adica {self.max_meaning}) la urmatoarea intrebare din perspectiva persoanei tale. Intrebare: '{question_text}'"}
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=self.messages
        )

        json_answer = response.choices[0].message.content
        data = json.loads(json_answer)

        self.messages.append(
            {"role": "assistant", "content": data['reason']}
        )
        print(data['reason'])
        return data["number"]
    
