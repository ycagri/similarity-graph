import uuid
from unittest import TestCase

from dotenv import load_dotenv

from src.graph import Node, Edge, Graph, EdgeType, NodeType
from src.graph_commons_connector import GraphCommonsConnector


class TestGraphCommonsConnector(TestCase):
    def test_create_graph(self):
        load_dotenv(".env")
        connector = GraphCommonsConnector()
        node_type = NodeType(id=uuid.uuid4(), name="Default Node", color="Black")
        edge_type = EdgeType(
            id=uuid.uuid4(),
            name="Default Edge",
            color="Black",
            directed=True,
            sourceNodeTypeId=node_type.id,
            targetNodeTypeId=node_type.id,
        )
        first_node_id = uuid.uuid4()
        second_node_id = uuid.uuid4()
        first_node = Node(
            id=first_node_id, degree=1, name="Node 1", typeId=node_type.id
        )
        second_node = Node(
            id=second_node_id, degree=1, name="Node 2", typeId=node_type.id
        )
        edge = Edge(
            id=uuid.uuid4(),
            description="Edge",
            name="Edge",
            sourceId=first_node_id,
            targetId=second_node_id,
            weight=5.0,
            typeId=edge_type.id,
        )
        graph = Graph(
            id=uuid.uuid4(),
            name="Test Graph",
            description="Test Graph",
            accessLevel=0,
            nodes=[first_node, second_node],
            nodeTypes=[node_type],
            edges=[edge],
            edgeTypes=[edge_type],
        )
        [graph_id, name] = connector.create_graph(graph)
        assert name == "Test Graph"
        assert connector.delete_graph(graph_id)
