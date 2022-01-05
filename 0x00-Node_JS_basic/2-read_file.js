const fs = require('fs');

// separated into sections from task reqs
const countStudents = (path) => {
    if (!fs.existsSync(path)) {
	throw Error('Cannot load the database');
    }
    
    const FileContents = fs.readFileSync(path, 'utf8');
    let arr = FileContents.toString().split(/\r?\n/); // split the array into indiv lines 
    arr = arr.filter((line) => line !== '');
    arr.shift(); // remove first element in the array and return the elem
    console.log(`Number of students: ${arr.length}`);

    // freecodecamp.org/news/javascript-split-how-to-split-a-string-into-an-array-in-js/
    // youtube.com/watch?v=4_iT6EGkQfk
    // blog.kevinchisholm.com/javascript/array-prototype/shift/
    

    const locateCS = arr.filter((line) => line.endsWith('CS')).map((line) => {
	const CSpeeps = line.split(',');
	return CSpeeps[0];
    });
    console.log(`Number of students in CS: ${locateCS.length}. List: ${locateCS.join(', ')}`);
    

    const locateSWE = arr.filter((line) => line.endsWith('SWE')).map((line) => {
	const SWEpeeps = line.split(',');
	return SWEpeeps[0];
    });
    console.log(`Number of students in SWE: ${locateSWE.length}. List: ${locateSWE.join(', ')}`);
};
module.exports = countStudents;
