const fs = require('fs');

// const readThat = fs.readFileSync('./txt/input.txt', 'utf-8');
// console.log(readThat);

// const textOut = `This is about Riot Games: ${readThat}.\n Created on ${Date.now()}`;
// fs.writeFileSync('./txt/output.txt', textOut);
// console.log('File modified'); 

//asynchronous 

fs.readFile('./txt/start.txt','utf-8',(err,data1) => {
    if (err) return console.log("Error occured 🙄")
    fs.readFile(`./txt/${data1}.txt`,'utf-8',(err,data2) => {
        console.log(data2);
        fs.readFile('./txt/append.txt','utf-8',(err,data3) => {
            console.log(data3);
            fs.writeFile('./txt/final.txt',`${data2}\n${data3}`,'utf-8', err => {
                console.log('Your file has been written');
            })
        });
    });
});
console.log('Kaam karna lawde ♨️')