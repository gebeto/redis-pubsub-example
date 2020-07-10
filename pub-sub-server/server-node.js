const server = require('http').createServer();
const Redis = require("ioredis");
const redis = new Redis(6379, "localhost");

const io = require('socket.io')(server, {
	origins: '*:*',
	// path: '/test',
	serveClient: false,
	// below are engine.IO options
	pingInterval: 10000,
	pingTimeout: 5000,
	cookie: false,
});


// redis.psubscribe("user-updated:*", (err, count) => {
// 	if (err) console.log("ERROR:", err);
// 	console.log("Count:", count);
// });

redis.psubscribe("user:*", (err, count) => {
	if (err) console.log("ERROR:", err);
	console.log("Count:", count);
});

redis.on("pmessage", (pattern, channel, message) => {
	// console.log(`MESSSAGE(${channel}):`, message);
	// console.log('NEW MESSAGE |', pattern, channel, message);
	io.emit(channel, JSON.parse(message));
});

// setInterval(() => {
// 	io.emit("mess", "hello world!");
// }, 2000);

server.listen(3000, () => {
	console.log(`Server started on http://localhost:3000`);
});
