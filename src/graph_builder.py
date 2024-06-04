import random
import uuid

from src.graph import Node, NodeType, EdgeType, Edge, Graph


class GraphBuilder:
    colors = ["red", "blue", "green", "yellow", "cyan", "magenta", "purple", "pink"]
    node_map: dict[str, Node] = {}
    edges: list[Edge] = []
    node_types: list[NodeType] = []
    edge_types_map: dict[uuid, dict[uuid, EdgeType]] = {}

    def __init__(self):
        for color in self.colors:
            self.node_types.append(
                NodeType(id=uuid.uuid4(), name=f"{color} Node", color=color)
            )
        for source_type in self.node_types:
            self.edge_types_map[source_type.id] = {}
            for target_type in self.node_types:
                self.edge_types_map[source_type.id][target_type.id] = EdgeType(
                    id=uuid.uuid4(),
                    name="",
                    color="Black",
                    directed=True,
                    sourceNodeTypeId=source_type.id,
                    targetNodeTypeId=target_type.id,
                )

    def build(self, name: str, description: str, data: dict[str, list[str]]) -> Graph:
        for key, value in data.items():
            source_node = self._get_node(key)
            for v in value:
                target_node = self._get_node(v)
                edge_type = self.edge_types_map[source_node.typeId][target_node.typeId]
                self.edges.append(
                    Edge(
                        id=uuid.uuid4(),
                        description="Edge",
                        name="Edge",
                        sourceId=source_node.id,
                        targetId=target_node.id,
                        weight=2.0,
                        typeId=edge_type.id,
                    )
                )
        return Graph(
            id=uuid.uuid4(),
            name=name,
            description=description,
            accessLevel=0,
            nodes=list(self.node_map.values()),
            nodeTypes=self.node_types,
            edges=self.edges,
            edgeTypes=self._get_edge_types(),
        )

    def _get_node(self, name: str):
        if name in self.node_map:
            return self.node_map[name]
        else:
            node_type = random.choice(self.node_types)
            node = Node(id=uuid.uuid4(), degree=1, name=name, typeId=node_type.id)
            self.node_map[name] = node
            return node

    def _get_edge_types(self) -> list[EdgeType]:
        edge_types = []
        for value in self.edge_types_map.values():
            for edge in value.values():
                edge_types.append(edge)
        return edge_types
