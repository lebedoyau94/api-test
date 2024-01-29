from flask import Flask
from flask_graphql import GraphQLView
from graphql.user_schema import schema
from database.mysql_connection import init_db

app = Flask(__name__)

# Inicializa la base de datos
init_db()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == '__main__':
    app.run(debug=True)
