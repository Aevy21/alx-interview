#!/usr/bin/node
/* This script prints all characters of a Star Wars movie using the Star Wars API.*/


const axios = require('axios');
const process = require('process');

if (process.argv.length < 3) {
  console.error('Usage: print_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

const getMovieDetails = async (movieId) => {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error('Error fetching movie details:', error);
    process.exit(1);
  }
};

const getCharacterName = async (characterUrl) => {
  try {
    const response = await axios.get(characterUrl);
    return response.data.name;
  } catch (error) {
    console.error('Error fetching character name:', error);
    return null;
  }
};

const main = async (movieId) => {
  const movieDetails = await getMovieDetails(movieId);
  const characters = movieDetails.characters || [];

  for (const characterUrl of characters) {
    const name = await getCharacterName(characterUrl);
    if (name) {
      console.log(name);
    }
  }
};

main(movieId);
