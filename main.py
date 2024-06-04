import argparse
import json
import os
import sys

from dotenv import load_dotenv

from src.graph_builder import GraphBuilder
from src.graph_commons_connector import GraphCommonsConnector
from src.openai_connector import OpenAIConnector
from src.prompt_reader import PromptReader


def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Creates similarity graph", epilog="🕺💃"
    )

    parser.add_argument(
        "--name",
        type=str,
        help="A name for the similarity graph",
    )
    parser.add_argument(
        "--description",
        type=str,
        help="A description for the similarity graph",
    )
    parser.add_argument(
        "--skip_prompt",
        type=bool,
        action=argparse.BooleanOptionalAction,
        help="Skips OpenAI prompt part and uses previously generated answer file",
    )
    parser.add_argument(
        "--question_file",
        type=str,
        help="Path to the file contains questions which will be asked to OpenAI",
    )

    return parser


def get_openai_answers(name, question_file):
    prompt_reader = PromptReader(question_file)
    openai_connector = OpenAIConnector()
    answer = openai_connector.ask(prompt_reader.get_general_question())
    try:
        os.mkdir(f"files/{name}")
    except FileExistsError:
        pass
    with open(f"files/{name}/general_answer.txt", "w+") as f:
        f.write(answer)
    result_map = {}
    for line in answer.split("\n"):
        grouping_answer = openai_connector.ask(
            f"{prompt_reader.get_similarity_question()} {line}?"
        )
        result_map[line] = grouping_answer.split("\n")
    with open(f"files/{name}/grouping_answer.json", "w+") as f:
        json.dump(result_map, f)
    return result_map


def main():
    load_dotenv(".env")
    arg_parser = setup_parser()
    options = arg_parser.parse_args()
    name = options.name
    description = options.description
    if options.skip_prompt:
        with open(f"files/{options.name}/grouping_answer.json", "r") as f:
            data = json.load(f)
    else:
        data = get_openai_answers(options.name, options.question_file)
    graph_builder = GraphBuilder()
    graph_commons_connector = GraphCommonsConnector()
    [graph_id, name] = graph_commons_connector.create_graph(
        graph_builder.build(
            name=f"{name} Similarity", description=description, data=data
        )
    )
    print(f"{name} created on graphcommons.com with id {graph_id}")


if __name__ == "__main__":
    sys.exit(main())
