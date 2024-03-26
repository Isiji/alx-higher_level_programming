#!/usr/bin/node
/**this script displays the status of a code**/

const request = require('request');
const url = process.argv[2];
request.get(url, function(err, response){
    if (err) {
        console.error(err);
    }
    console.log('code:' + ' ' + response.statusCode);
});
