from dataclasses import dataclass


@dataclass
class Song:
    lyrics: str
    genre: str
    language: str

