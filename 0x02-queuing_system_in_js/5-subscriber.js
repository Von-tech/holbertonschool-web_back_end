// import redis

const redis = require('redis');

const client = redis.createClient();


client.on('error', (err) => { 
    console.log('Redis client not connected to the server: ', + err);

}).on('ready', () => {
    console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel')

client.on('message', (channel, message) => {
    if (channel === 'holberton school channel') console.log(message)
    if (message === 'KILL_SERVER') {
        client.unsubscribe()
        client.quit()
    }
})
