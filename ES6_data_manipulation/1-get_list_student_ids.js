export default function getListStudentIds(listOfObjects) {
  let listOfIds = [];
  if (Array.isArray(listOfObjects)) {
    listOfIds = listOfObjects.map((object) => object.id);
  }
  return listOfIds;
}
