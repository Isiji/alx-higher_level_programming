#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
movie_id = process.argv[2];

request(url + movie_id, function (err, response, body) {
    if (err) {
        console.error(err);
    } else if (response.statusCode === 200) {
        jsonresponse = JSON.parse(body);
        console.log(jsonresponse.title);
    } else {
        console.log('Error code: '+response.statusCode);
    }
});