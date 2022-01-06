const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const app = http.createServer(async (req, res) => {
  if (req.method === 'GET') {
    if (req.url === '/') {
      res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
      await countStudents(process.argv[2])
        .then((val) => {
          res.write('This is the list of our students\n');
          res.write(`Number of students: ${val.arr.length}\n`);
          res.write(`Number of students in CS: ${val.locateCS.length}. List: ${val.locateCS.join(', ')}\n`);
          res.write(`Number of students in SWE: ${val.locateSWE.length}. List: ${val.locateSWE.join(', ')}\n`);
          res.end();
        })
        .catch((err) => {
          res.write('This is the list of our students\n');
          res.end(err.message);
        });
    }
  }
});
app.listen(port);
module.exports = app;
