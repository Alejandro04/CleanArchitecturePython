from flask import Flask, jsonify, request
import jwt

from src.adapters.provider_repository_mysql import ProviderRepositoryMySQL
from src.use_cases.provider_use_case import ProviderUseCase
from src.domain.provider import Provider

from src.core.adapters.user_repository_mysql import UserRepositoryMySQL
from src.core.use_cases.user_use_case import UserUseCase
from src.core.domain.user import User
   
app = Flask(__name__)
app = Flask(__name__)
#app.config['SECRET_KEY'] = 'your-secret-key'  # Clave secreta para firmar y verificar tokens

Provider_repository = ProviderRepositoryMySQL()
Provider_usecase = ProviderUseCase(Provider_repository)
User_repository = UserRepositoryMySQL()
User_usecase = UserUseCase(User_repository)


@app.route("/token", methods=["POST"])
def create_token():
    username = "jhon_doe"
    password = "secreta"

    #user = User_usecase.auth(username, password)
    user = True

    if user:
        payload = {'username': username}
        #token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        return {'token': token}
    return "Usuario o contraseña inválida"
   
@app.route("/providers", methods=["GET"])
def get_all():
    Providers = Provider_usecase.get_all()
    return jsonify([p.to_dict() for p in Providers]), 200
   
@app.route("/providers", methods=["POST"])
def create():
    provider_data = request.json
    provider = Provider.from_dict(provider_data)
    provider_created = Provider_usecase.create(provider)
    return jsonify(provider_created.to_dict()), 201

@app.route("/providers/<int:id>", methods=["GET"])
def get_by_id(id):
    Provider = Provider_usecase.get_by_id(id)
    if Provider is None:
        return jsonify({"message": "Provider no encontrado"}), 404
    return jsonify(Provider.to_dict()), 200
   
@app.route("/providers/<int:id>", methods=["PUT"])
def update(id):
    provider_data = request.json
    provider = Provider.from_dict(provider_data)
    Provider_updated = Provider_usecase.update(id, provider)
    return jsonify(Provider_updated.to_dict()), 200

@app.route("/providers/<int:id>", methods=["DELETE"])
def delete(id):
    Provider_usecase.delete(id)
    return "", 204
   
if __name__ == "__main__":
    app.run()
