export default function getStudentsByLocation(students, location) {
  return students.filter((object) => object.location === location);
}
