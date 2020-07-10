const Redis = require("ioredis");

const redis = new Redis(6379, "localhost");

redis.psubscribe("message:*", (err, count) => {
	if (err) console.log("ERROR:", err);
	console.log("Count:", count);
});

redis.on("pmessage", (pattern, channel, message) => {
	console.log(`MESSSAGE(${channel}):`, message);
});