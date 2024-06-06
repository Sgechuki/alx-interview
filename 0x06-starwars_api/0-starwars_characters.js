#!/usr/bin/node

const request = require('request');
const url1 = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
let characters;

const req = (arr, i) => {
  if (i === arr.length) return;
  request(arr[i], (error1, response1, body1) => {
    if (error1) {
      console.log(error1);
    }
    const characterBody = JSON.parse(body1);
    console.log(characterBody.name);
    req(arr, i + 1);
  });
};

request(url1, (error, response, body) => {
  const responseBody = JSON.parse(body);
  if (error) {
    console.log(error);
  }
  characters = responseBody.characters;
  req(characters, 0);
});
