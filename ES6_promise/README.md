# ES6 Promises

## Author

* **Johann Kerbrat** - *Project creator*

## Implementation

* **Xavier J. Cruz** - *Project implementation*

## Resources
Read or watch:
- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript Promise: An introduction](https://web.dev/promises/)
- [Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
- [Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [Throw / Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

- Promises (how, why, and what)
- How to use the `then`, `resolve`, `catch` methods
- How to use every method of the Promise object
- Throw / Try
- The await operator
- How to use an `async` function

## Requirements
- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `js` extension
- Your code will be tested using `Jest` and the command `npm run test`
- Your code will be verified against lint using ESLint
- All of your functions must be exported

## Setup

### Install NodeJS 20.x.x
(in your home directory):

```bash
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
```

Verify the installation:

```bash
$ nodejs -v
v20.15.1
$ npm -v
10.7.0
```

### Install Jest, Babel, and ESLint
In your project directory:
- Install Jest: `npm install --save-dev jest`
- Install Babel: `npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli`
- Install ESLint: `npm install --save-dev eslint`

## Project Files
- `package.json`
- `babel.config.js`
- `utils.js`
- `.eslintrc.js`

Don't forget to run `$ npm install` when you have the `package.json`

## Response Data Format
`uploadPhoto` returns a response with the format:

```json
{
  "status": 200,
  "body": "photo-profile-1"
}
```

`createUser` returns a response with the format:

```json
{
  "firstName": "Guillaume",
  "lastName": "Salva"
}
```
