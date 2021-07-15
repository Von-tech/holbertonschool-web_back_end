export default function appendToEachArrayValue(array, appendString) {
  const theNewA = [];
  for (const idx of array) {
    const value = appendString + idx;
     theNewA.push(value);
  }
  return theNewA;
}
