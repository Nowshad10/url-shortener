# URL Shortener - LAP 4 Pair Project

### Contributors
- [Nowshad Ahmed](https://github.com/Nowshad10)
- [Alex Patient](https://github.com/aPatient97)

## Project Description
In this application, the user can enter a URL and receive a shortened one.
For example, if you input https://github.com/getfutureproof, you will receive back http://localhost:5000/LGFIm
The URL is then stored in a database, and doesn't allow any duplicates, so when you paste the original URL again, it will give back the same shortened one.

## Installation & Usage
### Installation
- Clone the repo.
- Run `pipenv shell` to create the virtual environment, and then run `pipenv install` to install all the relevant dependencies in the Pipfile.

### Usage
- In the terminal, run `pipenv run dev` to start the application at `http://localhost:5000`. 
- Type in a URL into the input field and press **shorten**.
- If you visit `http://localhost:5000/all` you can see all the URLs currently saved in the database.

## Wins & Challenges
### Wins
- URL shortener works as intended.
- Getting the redirect working.

### Challenges
- When deploying to Heroku, it deployed fine but posting to the database returns an Internal Server 500 Error.


