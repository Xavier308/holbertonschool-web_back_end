export default function appendToEachArrayValue(array, appendString) {
  const newarray = [];
  for (const element of array) {
    newarray.push(appendString + element);
  }

  return newarray;
}
