export default class HolbertonCourse {

  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  getstudents() {
    return this._students;
  }
  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('Name must be a string');
    this._name = newName;
  }
  set length(newLength) {
    if (typeof newLength === 'number') throw TypeError('Length must be a number');
    this._length = length;
  }

  set students(newStudents) {
    if (typeof newStudents === 'object' && newStudents.every((x) => typeof x === 'string')) 
	throw TypeError('Students must be an array of numbers');
    this._students = newStudents;
}
