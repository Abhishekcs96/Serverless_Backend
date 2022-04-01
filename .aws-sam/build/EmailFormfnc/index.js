const sendEmail = require('./sendEmail')
// Pass event object keys to the function sendEmail to get it processed,
// Once the promise is fullfilled, retrieve the response object from the promise
// which would indicate the email has been sent, invoke context.done to identify the email being sent.
// (callback allows us to execute code with the current context of the handler)
exports.handler = async (event, context) => {
    return sendEmail(event.name, event.message, event.email).then((response) => {context.done(null, 'Email sent');
        
    })
}
