#!/usr/bin/node


const fs = require('fs');
const request = require('request');

request.get(process.argv[1], (err, response, body) => {
    if (err) {
        console.error(err);
    } else {
        fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
            if (error) {
                console.error(err);
            }
        })}
})