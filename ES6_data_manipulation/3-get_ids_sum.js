export default function getStudentIdsSum(students) {
  const InitialValue = 0;
  return students.reduce((total, currentValue) => total + currentValue.id, InitialValue);
}
