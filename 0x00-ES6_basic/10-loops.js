export default function appendToEachArrayValue(array, appendString) {
  const array = [];
  for (const idx of array) {
    const value = appendString + idx;
     array.push(value);
  }
  return array;
}
