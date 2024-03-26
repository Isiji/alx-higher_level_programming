#!/usr/bin/node
// Number of films with the given character ID
const request = require('request');
let count = 0;

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => 
        character.endswith('/18')) 
          ? count += 1
          :count;
        
      }, 0));
    }
  });