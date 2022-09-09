import strawberry
from app import models
from app.api.matches.types import Match
from app.services import matches


class MatchNotFound(Exception):
    pass


@strawberry.type
class Query:
    @strawberry.field
    def matches() -> list["Match"]:
        matches_data: list["models.Match"] = matches.get_matches()
        return [Match.marshal(match_data) for match_data in matches_data]

    @strawberry.field
    def match(self, match_id: int) -> Match | None:
        try:
            match_data = matches.get_match(match_id)
            return Match.marshal(match_data)
        except MatchNotFound:
            return None

    @strawberry.field
    def recent_match(self) -> Match | None:
        try:
            match_data = matches.get_recent_match()
            return Match.marshal(match_data)
        except MatchNotFound:
            return None

    # recent match
    # my matches
