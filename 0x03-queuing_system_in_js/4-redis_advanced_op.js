import { createClient, print } from 'redis';

const client = createClient();

client.hset("HolbertonSchools", "Portland", 50, print);
client.hset("HolbertonSchools", "Seattle", 80, print);
client.hset("HolbertonSchools", "New York", 20, print);
client.hset("HolbertonSchools", "Bogota", 20, print);
client.hset("HolbertonSchools", "Cali", 40, print);
client.hset("HolbertonSchools", "Paris", 2, print);

client.hgetall("HolbertonSchools", function(err, reply) {
  console.log(reply);
});
