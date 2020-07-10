import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
pubsub = r.pubsub()
pubsub.subscribe("message")

for message in pubsub.listen():
	print("MESSAGE:", message)