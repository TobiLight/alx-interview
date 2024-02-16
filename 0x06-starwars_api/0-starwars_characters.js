#!/usr/bin/node
/**
 * File; 0-starwars_characters.js
 * Author: Oluwatobiloba Light
 * Description: Prints all characters of a Star Wars movie
 */

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';
const movieID = process.argv[2];

const getMovieCharacters = (apiURL, movieId) => {
  if (process.argv.length >= 2) {
    if (!movieId) { process.exit(1); }

    request(apiURL + '/films/' + movieId, async (err, _, body) => {
      if (err) { console.log(err); }

      const resp = JSON.parse(body).characters;

      const movieCharactersResp = resp.map(characterURL => new Promise((resolve, reject) => {
        request(characterURL, (promiseErr, _, promiseResp) => {
          if (promiseErr) { reject(promiseErr); }

          resolve(JSON.parse(promiseResp).name);
        });
      }));

      Promise.all(movieCharactersResp).then(res => console.log(res.join('\n'))).catch(err => err);
    });
  }
};

getMovieCharacters(API_URL, movieID);
