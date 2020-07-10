import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
pubsub = r.pubsub()

while True:
	message = input("Message: ")
	if not message: break
	splitted = message.split("::")
	if len(splitted) == 2:
		rediska.r.publish(f"message:{splitted[0]}", splitted[1])
	else:
		rediska.r.publish("message:111", message)

# for message in pubsub.listen():
# 	print("MESSAGE:", message)