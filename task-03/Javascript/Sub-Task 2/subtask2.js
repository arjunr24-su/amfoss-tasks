const fs = require('fs');
const data = fs.readFileSync('input.txt', 'utf8');
fs.writeFileSync('output.txt', data);
