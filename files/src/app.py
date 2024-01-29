from flask import Flask, request, jsonify
import graphene

# Definición del esquema GraphQL usando Graphene
class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info, name):
        return f'Hello {name}'

schema = graphene.Schema(query=Query)

# Creación de la aplicación Flask
app = Flask(__name__)

# Ruta para manejar las solicitudes GraphQL
@app.route('/graphql', methods=['GET', 'POST'])
def graphql():
    # Obtener la consulta (query) de la solicitud
    data = request.json
    query = data.get('query')
    variables = data.get('variables')

    # Ejecutar la consulta usando el esquema
    result = schema.execute(query, variable_values=variables)

    # Manejar errores en la consulta
    if result.errors:
        response = {
            'errors': [str(error) for error in result.errors]
        }
    else:
        response = {
            'data': result.data
        }

    # Devolver la respuesta como JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run()
