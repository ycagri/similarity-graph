from __future__ import (
    annotations,  # To allow BaseMappableModel to be used within its own class
)

from uuid import UUID

from pydantic import BaseModel as _BaseModel


class Graph(_BaseModel):
    id: UUID
    accessLevel: int
    description: str
    name: str
    edges: list[Edge]
    edgeTypes: list[EdgeType]
    nodes: list[Node]
    nodeTypes: list[NodeType]


class Edge(_BaseModel):
    id: UUID
    name: str
    sourceId: UUID
    targetId: UUID
    weight: float
    typeId: UUID


class Node(_BaseModel):
    id: UUID
    degree: int
    name: str
    typeId: UUID


class EdgeType(_BaseModel):
    id: UUID
    name: str
    color: str
    directed: bool
    sourceNodeTypeId: UUID
    targetNodeTypeId: UUID


class NodeType(_BaseModel):
    id: UUID
    color: str
    name: str
