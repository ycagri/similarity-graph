import os

import requests

from src.graph import Graph


class GraphCommonsConnector:
    GRAPH_COMMONS_END_POINT = "https://graphcommons.com/graphql"

    api_key: str

    def __init__(self):
        email = os.environ.get("GRAPH_COMMONS_EMAIL")
        password = os.environ.get("GRAPH_COMMONS_PASSWORD")
        response = requests.post(
            self.GRAPH_COMMONS_END_POINT,
            json={
                "query": "mutation($loginOrEmail: ID!, $password: String!) {login("
                "loginOrEmail: $loginOrEmail, password: $password)}",
                "variables": {"loginOrEmail": email, "password": password},
            },
        )
        self.api_key = response.json()["data"]["login"]

    def create_graph(self, graph: Graph):
        response = requests.post(
            self.GRAPH_COMMONS_END_POINT,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "query": "mutation($graph: GraphInput!) {createGraph(graph: $graph) {"
                "graph{id name description image}}}",
                "variables": {"graph": graph.model_dump(mode="json")},
            },
        )
        graph = response.json()["data"]["createGraph"]["graph"]
        return [graph["id"], graph["name"]]

    def delete_graph(self, graph_id: str) -> bool:
        response = requests.post(
            self.GRAPH_COMMONS_END_POINT,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "query": "mutation($deleteGraphId: String!) {deleteGraph(id: $deleteGraphId) {"
                "errors success}}",
                "variables": {"deleteGraphId": graph_id},
            },
        )
        return response.json()["data"]["deleteGraph"]["success"]
