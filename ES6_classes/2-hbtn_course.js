export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = typeof name === 'string' ? name : (() => { throw new Error('Please enter a string'); })();
    this._length = typeof length === 'number' ? length : (() => { throw new Error('Please enter a number'); })();
    this._students = Array.isArray(students) ? students : (() => { throw new Error('Please enter a an array'); })();
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new Error('Please enter a string');
    }
  }

  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof length === 'number') {
      this._length = length;
    } else {
      throw new Error('Please enter a number');
    }
  }

  get students() {
    return this._students;
  }

  set students(students) {
    if (Array.isArray(students)) {
      this._students = students;
    } else {
      throw new Error('Please enter an array');
    }
  }
}
