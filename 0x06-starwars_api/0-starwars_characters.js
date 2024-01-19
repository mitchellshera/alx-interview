#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const filmEndpoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;

const getCharacterNames = async () => {
  try {
    const filmResponse = await getRequest(filmEndpoint);
    const characters = filmResponse.characters;

    if (!characters || characters.length === 0) {
      throw new Error('Error: Got no Characters for some reason');
    }

    const characterNames = await Promise.all(characters.map(url => getRequest(url).then(data => data.name)));
    return characterNames;
  } catch (error) {
    console.error(error.message);
  }
};

const getRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(`Error: ${error || `Status Code: ${response.statusCode}`}`);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const printCharacterNames = async () => {
  const characterNames = await getCharacterNames();

  if (characterNames) {
    characterNames.forEach((name, index) => {
      process.stdout.write(name + (index === characterNames.length - 1 ? '' : '\n'));
    });
  }
};

printCharacterNames();
