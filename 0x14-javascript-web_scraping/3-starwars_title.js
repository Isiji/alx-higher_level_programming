#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, function (err, response, body) {
    if (err) {
        console.error(err);
    } else if (response.statusCode === 200) {
        const jsonresponse = JSON.parse(body);
        console.log(jsonresponse.title);
	}
});
