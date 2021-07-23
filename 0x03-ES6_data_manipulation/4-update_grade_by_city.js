export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  if (!(studentsList instanceof Array)) {
    return [];
}

function addScore(student) {
  for (const person in newGrades) {
    if (person.studentId === student.id) {
      myArr.push(person.grade);
    }
  });
  if (student.grade === undefined) {
    student.grade = 'N/A';
  }
  return student;
}
const filteredStudentList = studentsList.filter((students) => students.location === city);
return filteredStudentList.map(addScore);
}
// Create a function updateStudentGradeByCity that returns an array of students for a specific city with their new grade
// It should accept a list of students (from getListStudents), a city (String), and newGrades (Array of “grade” objects) as parameters
// PLD HELP 7/23 10:50 A.M.
