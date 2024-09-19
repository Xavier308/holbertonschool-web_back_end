const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const dbpath = process.argv[2];
  let o = 'This is the list of our students\n';
  if (!dbpath) {
    o += 'Cannot load the database';
    res.status(500).send(o);
    return;
  }
  try {
    const studentsData = await countStudents(dbpath);
    o += studentsData;
    res.send(o);
  } catch (error) {
    o += 'Cannot load the database';
    res.send(o);
  }
});

app.listen(1245, () => {
  console.log('Express server is listening on port 1245');
});

module.exports = app;
