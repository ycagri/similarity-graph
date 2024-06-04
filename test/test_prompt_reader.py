from unittest import TestCase

from src.prompt_reader import PromptReader


class TestPromptReader(TestCase):
    def test_general_and_similarity_read(self):
        reader = PromptReader("files/battle.json")
        assert reader.get_general_question() == (
            "I want you to list 100 famous historical battles all around the "
            "world. I just want the names of the battles line by line, no extra "
            "text, no numbers in the beginning."
        )
        assert reader.get_similarity_question() == (
            "Now forget everything! I just want the names of the battles line "
            "by line, no extra text, no bullets or numbers in the beginning. I "
            "want you to list 5 of battles similar to "
        )
