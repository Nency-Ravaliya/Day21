const http = require('http');
const port = 3001;

const requestListener = function (req, res) {
  res.writeHead(200);
  res.end('Welcome to the world pf Cloud & DevOps');
};

const server = http.createServer(requestListener);
server.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
