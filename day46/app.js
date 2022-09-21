const express = require('express');
const fs = require('fs')
const app = express();

//middleware
app.use(express.json());

app.get('/',(req,res) => {
    res.status(200).json({message:"Hello server", app:'Faunatious'});
});

app.post('/', (req,res) => {
    res.send("You can post to this endpoint");
});

const tours = JSON.parse(
    fs.readFileSync(`${__dirname}/dev-data/data/tours-simple.json`)
);

app.get('/api/v1/tours', (req,res) => {
    res.status(200).json({
        status: 'success',
        results: tours.length,
        data: {
            tours
        }
    });
});

app.post('/api/v1/tours', (req,res) => {
    console.log(req.body);
    //body of the request is empty for now but getting updated in postman
    res.send("Done")
})

const port = 3000;

app.listen(port, () => {
    console.log(`App running on port no. ${port}`)
});