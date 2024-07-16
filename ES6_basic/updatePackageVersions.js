// This script automatically fills with the correct version dependency in your local machine XCS
// The file package.json needs to have the old info **

// For ES6 basics project (Holberton)
// in file package.json use this line version --> "eslint": "^7.2.0" to solve problem when usin 'npm install' command.

const fs = require('fs');
const path = require('path');

const packageJsonPath = path.join(__dirname, 'package.json');
const packageJson = require(packageJsonPath);

// Function to fetch the version of a package
function getPackageVersion(packageName) {
  const packagePath = path.join(__dirname, 'node_modules', packageName, 'package.json');
  if (fs.existsSync(packagePath)) {
    const packageJson = require(packagePath);
    return packageJson.version;
  }
  return null;
}

// Update devDependencies versions
for (let packageName in packageJson.devDependencies) {
  const version = getPackageVersion(packageName);
  if (version) {
    // Update the version in package.json to the current version installed
    packageJson.devDependencies[packageName] = `^${version}`;
  }
}

// Write the updated package.json back to file
fs.writeFileSync(packageJsonPath, JSON.stringify(packageJson, null, 2), 'utf8');
console.log('Updated package.json with current versions of packages.');
