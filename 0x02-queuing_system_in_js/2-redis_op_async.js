// import redis
const { promisify } = require('util')


const redis = require('redis');

const client = redis.createClient();

const asyncSet = promisify(client.set).bind(client)
const asyncGet = promisify(client.get).bind(client)



client.on('error', (err) => { 
    console.log('Redis client not connected to the server: ', + err);

}).on('ready', () => {
    console.log('Redis client connected to the server');
});

const setNewSchool = async (schoolName, value) => console.log(`Reply: ${await asyncSet(schoolName, value)}`)
const displaySchoolValue = async (schoolName) => console.log(await asyncGet(schoolName))

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
