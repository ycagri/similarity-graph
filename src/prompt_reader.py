import json


class PromptReader:
    def __init__(self, path):
        with open(path) as f:
            self.prompts = json.load(f)

    def get_general_question(self) -> str:
        return self.prompts["general"]

    def get_similarity_question(self) -> str:
        return self.prompts["similarity"]
