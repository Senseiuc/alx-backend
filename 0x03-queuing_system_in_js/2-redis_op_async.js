#!/usr/bin/node
/**
 * Connect to redis server via redis client
 */
import { promisify } from 'util';
import { createClient, print } from 'redis';

const client = createClient();

client.on('error',
  err => console.log('Redis client not connected to the server: ',
    err.toString()));

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  const value = await getAsync(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
