# redis-pubsub-example
Redis PubSub example with Node.js and Python


## Configure Python
```sh
python3 -m venv venv
source venv
pip install -r requirements.txt
```

### Run `publisher.py`
```sh
python src/publisher.py
```

### Run `subscriber.py`
```sh
python src/subscriber.py
```


## Configure Node.js
```sh
yarn install
```

### Run `subscriber.js`
```sh
node src/subscriber.js
```