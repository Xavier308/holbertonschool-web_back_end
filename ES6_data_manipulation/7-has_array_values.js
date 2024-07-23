export default function hasValuesFromArray(set, array) {
  let status = true;
  array.map((element) => {
    if (set.has(element)) {
      status = true;
    } else {
      status = false;
    }
    return status;
  });
  return status;
}
