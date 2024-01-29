import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.user import User as UserModel

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.Int())

    def resolve_user(self, info, id):
        query = User.get_query(info)
        return query.get(id)

schema = graphene.Schema(query=Query)
