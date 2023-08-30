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

client.on('message', (channel, message) => {
  console.log(message);
  if (message == 'KILL_SERVER'){
    client.unsubscribe();
    client.quit();
  }
});

client.subscribe("holberton school channel")
