from unittest import TestCase

from src.openai_connector import OpenAIConnector
from dotenv import load_dotenv


class TestOpenAIConnector(TestCase):
    def test_ask(self):
        load_dotenv(".env")
        connector = OpenAIConnector()
        answer = connector.ask("Say this is a test!")
        assert answer == "This is a test!"
