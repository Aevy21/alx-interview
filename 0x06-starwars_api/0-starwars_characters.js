#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function requestCharacter (characterUrlList, idx) {
  if (idx === characterUrlList.length) {
    return;
  }

  request(characterUrlList[idx], (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const characterName = JSON.parse(body).name;
      console.log(characterName);

      requestCharacter(characterUrlList, idx + 1);
    }
  });
}

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const charactersUrls = JSON.parse(body).characters;
    requestCharacter(charactersUrls, 0);
  }
});
