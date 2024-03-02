#!/usr/bin/node
const request = require('request');


function getCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Status:', response.statusCode);
      } else {
        const film = JSON.parse(body);
        film.characters.forEach((characterUrl) => {
          request(characterUrl, (error, response, body) => {
            if (error) {
              console.error('Error:', error);
            } else if (response.statusCode !== 200) {
              console.error('Status:', response.statusCode);
              } else {
                const character = JSON.parse(body);
                console.log(character.name);
                }
          });
      });
    }
  });
}

const movieId = process.argv[2];

if (!movieId) {
    console.error('Please provide a movie ID as an argument.');
} else {
    getCharacters(movieId);
}
