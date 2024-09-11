const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
readline.question('Enter a number: ', n => {
    n = parseInt(n);
    for (let i = 0; i < n; i++) {
        console.log(' '.repeat(n - i - 1) + '*'.repeat(2 * i + 1));
    }
    for (let i = n - 2; i >= 0; i--) {
        console.log(' '.repeat(n - i - 1) + '*'.repeat(2 * i + 1));
    }
    readline.close();
});