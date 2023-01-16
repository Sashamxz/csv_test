// Require the Elasticsearch library.
const elasticsearch = require('elasticsearch');

// Instantiate an Elasticsearch client.
const client = new elasticsearch.Client({
  hosts: ['http://localhost:9200'],
});

// Ping the client to be sure Elasticsearch is up.
client.ping(
  {
    requestTimeout: 30000,
  },
  function (error) {
    // At this point, Elasticsearch is down, please check your Elasticsearch service.
    if (error) {
      console.error('Elasticsearch cluster is down!');
    } else {
      console.log('Everything is okay.');
    }
  }
);

client.indices.create(
    {
      index: 'example_index',
    },
    function (error, response, status) {
      if (error) {
        console.log(error);
      } else {
        console.log('Created a new index.', response);
      }
    }
  );