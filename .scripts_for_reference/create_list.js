// npm install node-appwrite --save

const sdk = require('node-appwrite');

// Init SDK
let client = new sdk.Client();

let database = new sdk.Database(client);

client
    .setEndpoint('https://[HOSTNAME]/v1') // Your API Endpoint
    .setProject('') // Your project ID
    .setKey('') // Your secret API key
    .setSelfSigned()
;

let promise = database.createDocument('61eafd364852a5bccadb', 'unique()', {'emails': 'achintya_x7.3@gmail.com'});

promise.then(function (response) {
    console.log(response);
}, function (error) {
    console.log(error);
});
