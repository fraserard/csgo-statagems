from datetime import datetime, timedelta

import strawberry
from flask import after_this_request
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    get_jwt_identity,
    set_access_cookies,
)
from graphql.error.graphql_error import format_error as format_graphql_error
from strawberry.flask.views import GraphQLView
from strawberry.http import GraphQLHTTPResponse
from strawberry.schema.config import StrawberryConfig
from strawberry.types import ExecutionResult

from app.api.maps.mutation import Mutation as MapsMutation
from app.api.maps.query import Query as MapsQuery
from app.api.matches.mutation import Mutation as MatchesMutation
from app.api.matches.query import Query as MatchesQuery
from app.api.players.mutation import Mutation as PlayersMutation
from app.api.players.query import Query as PlayersQuery


class FlaskGraphQLView(GraphQLView):

    # https://flask-jwt-extended.readthedocs.io/en/stable/refreshing_tokens/

    def process_result(self, result: ExecutionResult) -> GraphQLHTTPResponse:
        @after_this_request
        def refresh_expiring_jwts(response):
            try:
                exp_timestamp = get_jwt()["exp"]
                now = datetime.utcnow()
                target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
                if target_timestamp > exp_timestamp:
                    access_token = create_access_token(identity=get_jwt_identity())
                    set_access_cookies(response, access_token)
                return response
            except (RuntimeError, KeyError):
                # Case where there is not a valid JWT. Just return the original respone
                return response

        data: GraphQLHTTPResponse = {"data": result.data}

        if result.errors:
            data["errors"] = [format_graphql_error(err) for err in result.errors]
        
        return data


@strawberry.type
class Query(PlayersQuery, MatchesQuery, MapsQuery):
    pass


@strawberry.type
class Mutation(MatchesMutation, PlayersMutation, MapsMutation):

    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=True),
)
