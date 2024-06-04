from unittest import TestCase

from src.graph_builder import GraphBuilder


class TestGraphBuilder(TestCase):
    def test_build(self):
        graph_builder = GraphBuilder()
        graph = graph_builder.build(
            name="Test",
            description="Test Description",
            data={
                "Node 1": ["Node 2", "Node 3"],
                "Node 2": ["Node 3"],
                "Node 3": ["Node 1"],
            },
        )
        assert graph.name == "Test"
        assert graph.description == "Test Description"
        assert len(graph.nodes) == 3
        assert len(graph.edges) == 4
        assert len(graph.nodeTypes) == 8
        assert len(graph.edgeTypes) == 64
