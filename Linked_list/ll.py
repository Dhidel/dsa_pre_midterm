from __future__ import annotations
from typing import Any, Dict, Iterable, Iterator, List, Optional


class Node:
    def __init__(self, name: str, artist: str, album: str) -> None:
        self.data: Dict[str, str] = {
            "name": name,
            "artist": artist,
            "album": album
        }
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.data['name']!r} by {self.data['artist']!r})"


class LinkedList:
    def __init__(self) -> None:
        self.start: Optional[Node] = None
        self.end: Optional[Node] = None

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
            parts.append(f"[{node.data['name']}]")
        parts.append("NIL")
        return " <-> ".join(parts)

    def insert_at_beginning(self, name: str, artist: str, album: str) -> None:
        new_node = Node(name, artist, album)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.next = self.start
            self.start.prev = new_node
            self.start = new_node

    def insert_at_end(self, name: str, artist: str, album: str) -> None:
        new_node = Node(name, artist, album)
        if self.start is None:
            self.start = new_node
            self.end = new_node
            return

        assert self.end is not None
        new_node.prev = self.end
        self.end.next = new_node
        self.end = new_node

    def delete_node(self, song_name: str) -> bool:
        if self.start is None:
            return False

        for node in self:
            if node.data["name"] == song_name:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.start = node.next

                if node.next:
                    node.next.prev = node.prev
                else:
                    self.end = node.prev
                
                node.next = None
                node.prev = None
                return True
        return False

    def search(self, song_name: str) -> Optional[Node]:
        for node in self:
            if node.data["name"] == song_name:
                return node
        return None

    @classmethod
    def from_iterable(cls, songs: Iterable[Dict[str, str]]) -> LinkedList:
        ll = cls()
        for song in songs:
            ll.insert_at_end(song["name"], song["artist"], song["album"])
        return ll