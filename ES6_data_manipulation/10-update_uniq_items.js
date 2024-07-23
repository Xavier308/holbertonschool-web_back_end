export default function updateUniqueItems(map) {
  function logMapElements(value, key) {
    if (value === 1) {
      map.set(key, 100);
    }
  }
  if (map instanceof Map) {
    map.forEach(logMapElements);
  } else {
    throw new Error('Cannot process');
  }
}
