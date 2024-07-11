#!/usr/bin/node
// This script prints all characters of a Star Wars movie using the Star Wars API.

const request = require('request');
const process = require('process');

if (process.argv.length < 3) {
  console.error('Usage: print_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

const getMovieDetails = (movieId, callback) => {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie details:', error);
      process.exit(1);
    }
    callback(JSON.parse(body));
  });
};

const getCharacterName = (characterUrl, callback) => {
  request(characterUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching character name:', error);
      callback(null);
      return;
    }
    callback(JSON.parse(body).name);
  });
};

const main = (movieId) => {
  getMovieDetails(movieId, (movieDetails) => {
    const characters = movieDetails.characters || [];
    let count = 0;

    characters.forEach((characterUrl) => {
      getCharacterName(characterUrl, (name) => {
        if (name) {
          console.log(name);
        }
        count++;
        if (count === characters.length) {
          process.exit(0);
        }
      });
    });
  });
};

main(movieId);
