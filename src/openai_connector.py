import os

from openai import OpenAI


class OpenAIConnector:
    client: OpenAI

    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def ask(self, question: str):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}]
        )
        return completion.choices[0].message.content
