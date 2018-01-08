const express = require('express');
const os = require('os');

const app = express();
global.hostname = os.hostname();
const port = 8080;
// const HOST = 'localhost';

app.set('view engine', 'ejs');
app.use('/src', express.static('src'));
app.use('/dist', express.static('dist'));

if(typeof process.env.TODO_BACKEND_URL === 'undefined') {
  global.todoBackendUrl = 'http://localhost:8000/api/todo-list/'
} else {
  global.todoBackendUrl = process.env.TODO_BACKEND_URL;
}



app.get('/', function(req, res) {
  res.render('index', {apiUrl: todoBackendUrl, hostname: hostname});
});

app.listen(port);
//console.log(`Running on http://${hostname}:${port}`);
