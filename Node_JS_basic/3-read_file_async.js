const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      // Remove the header (first line)
      lines.shift();

      const students = {};
      let totalStudents = 0;

      lines.forEach((line) => {
        const [firstname, , , field] = line.split(',');

        if (!firstname || !field) {
          return;
        }

        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
        totalStudents += 1;
      });

      // Log the total number of students
      console.log(`Number of students: ${totalStudents}`);

      // Log each field with the respective number of students and list of names
      for (const field in students) {
        if (Object.prototype.hasOwnProperty.call(students, field)) {
          const studentList = students[field];
          console.log(
            `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`,
          );
        }
      }

      resolve();
    });
  });
}

module.exports = countStudents;
