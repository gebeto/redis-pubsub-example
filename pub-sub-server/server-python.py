from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.exceptions import HTTPNotFound


import redis
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)
pubsub = r.pubsub()


def publish_json(m_type, data):
	return r.publish(m_type, json.dumps(data))


USERS = {
	"1": { "id": 1, "name": "Slavik" },
}


@view_config(route_name='index')
def index(request):
	return Response(body=open("index.html").read())


@view_config(route_name='users', renderer='json')
def users(request):
	return USERS


@view_config(route_name='users_add', renderer='json')
def users_add(request):
	data = request.GET
	new_user = { "id": len(USERS) + 1, "name": data["name"] }
	USERS[str(new_user["id"])] = new_user
	# publish_json(f"user-added:{new_user['id']}", new_user)
	publish_json(f"user:added", new_user)
	return USERS


@view_config(route_name='users_update', renderer='json')
def users_update(request):
	data = request.GET
	user = USERS.get(data["id"])
	if user:
		user["name"] = data["name"]
		publish_json(f"user:updated", user)
	else:
		raise HTTPNotFound()
	return USERS


if __name__ == '__main__':
	config = Configurator()

	config.add_route('index', '/')
	config.add_route('users', '/users')
	config.add_route('users_add', '/users/add')
	config.add_route('users_update', '/users/update')

	config.scan()

	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 6543, app)
	server.serve_forever()