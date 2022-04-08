const sendEmail = require("./sendEmail");
// Pass event object keys to the function sendEmail to get it processed,
// Once the promise is fullfilled, retrieve the response object from the promise
// No need for callbacks, just signal end with promise resolution in a return statement.(callback allows us to execute code with the current context of the handler)
exports.handler = async (event, context) => {
  return sendEmail(event.name, event.message, event.email).then((response) => "Email sent");
};
