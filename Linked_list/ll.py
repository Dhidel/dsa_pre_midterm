from __future__ import annotations
from typing import Any, Iterable, Iterator, List, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.data!r})"


class LinkedList:
    def __init__(self) -> None:
        self.start: Optional[Node] = None

    def __iter__(self) -> Iterator[Node]:
        node = self.start
        while node is not None:
            yield node
            node = node.next

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        parts: List[str] = ["START"]
        for node in self:
            parts.append(repr(node.data))
        parts.append("NIL")
        return "\n" + " --> ".join(parts)

    def traverse(self) -> None:
        for node in self:
            print(node.data)

    def insert_at_beginning(self, element: Node) -> None:
        element.next = self.start
        self.start = element

    def insert_at_end(self, element: Node) -> None:
        element.next = None
        if self.start is None:
            self.start = element
            return
        
        tail = self.start
        for node in self:
            tail = node
        tail.next = element

    def insert_after_node(self, element: Node, node_reference: Any) -> bool:
        target: Optional[Node] = None
        for n in self:
            if (n is node_reference) if isinstance(node_reference, Node) else (n.data == node_reference):
                target = n
                break

        if target is None:
            return False

        element.next = target.next
        target.next = element
        return True

    def delete_node(self, element_data: Any) -> bool:
        if self.start is None:
            return False

        if self.start.data == element_data:
            to_remove = self.start
            self.start = self.start.next
            to_remove.next = None
            return True

        prev = self.start
        for cur in self:
            if cur.data == element_data:
                prev.next = cur.next
                cur.next = None
                return True
            prev = cur

        return False

    def search(self, element_data: Any) -> Optional[Node]:
        for n in self:
            if n.data == element_data:
                return n
        return None

    def to_list(self) -> List[Any]:
        return [n.data for n in self]

    @classmethod
    def from_iterable(cls, iterable: Iterable[Any]) -> LinkedList:
        ll = cls()
        tail: Optional[Node] = None
        for item in iterable:
            node = Node(item)
            if ll.start is None:
                ll.start = node
            else:
                assert tail is not None
                tail.next = node
            tail = node
        return ll