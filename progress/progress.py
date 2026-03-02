from typing import List, Tuple
import requests
import os
from pydantic import BaseModel


class Track(BaseModel):
    # slug: str
    title: str
    # course: bool
    # num_concepts: int
    num_exercises: int
    # web_url: str
    # icon_url: str
    # tags: List[str]
    # last_touched_at: DateSchema
    # is_new: bool
    is_joined: bool
    # num_learnt_concepts: int
    num_completed_exercises: int
    # has_notifications: bool
    # links: List[str]


class JoinedTracks(BaseModel):
    tracks: List[Track]


API_BASE_URL = "https://exercism.org/api/v2"


def get_default_headers() -> dict:
    token = os.getenv("EXERCISM_TOKEN")
    assert token is not None

    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "MrAditya github action. See https://github.com/MrAdityaAlok/learn-to-program",
    }


def get_joined_tracks() -> JoinedTracks:
    response = requests.get(
        API_BASE_URL + "/tracks?status=joined", headers=get_default_headers()
    )
    assert response.status_code == 200
    return JoinedTracks.model_validate(response.json())


def get_progress() -> List[Tuple[str, float]]:
    return [
        (track.title, track.num_completed_exercises / track.num_exercises * 100)
        for track in get_joined_tracks().tracks
    ]
