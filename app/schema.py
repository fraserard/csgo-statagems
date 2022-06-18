import strawberry
from strawberry.schema.config import StrawberryConfig

from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended.utils import get_jwt_identity

from app.api.players.query import Query as PlayersQuery
from app.api.matches.query import Query as MatchesQuery
from app.api.matches.mutation import Mutation as MatchesMutation

# class MyGraphQLView(GraphQLView):
#     @jwt_required()
#     def get_context(self, request: Request) -> Any:
#         id, role = [get_jwt_identity[k] for k in ('id','role')]
#         return {'request': request, 'id': id, 'role': role}


@strawberry.type
class Query(PlayersQuery, MatchesQuery):
    pass


@strawberry.type
class Mutation(MatchesMutation):
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(auto_camel_case=True),
)
