console.log('Welcome to Holberton School, what is your name?');

process.stdin.setEncoding('utf-8');

process.stdin.on('readable', () => {
  const inputData = process.stdin.read();
  if (inputData !== null) {
    process.stdout.write(`Your name is: ${inputData}`);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
