import getStudentsByLocation from './2-get_students_by_loc';

export default function updateStudentGradeByCity(students, city, newGrades) {
  function checkGrades(newGrade, validStudents) {
    const student = validStudents.filter((student) => student.id === newGrade.studentId);
    student[0].grade = newGrade.grade;
    return student;
  }
  const validStudents = getStudentsByLocation(students, city);
  newGrades.map((newGrade) => checkGrades(newGrade, validStudents));
  validStudents.map((student) => {
    const newStudent = student;
    if (!student.grade) {
      newStudent.grade = 'N/A';
    }
    return newStudent;
  });
  return validStudents;
}
