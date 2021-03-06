require('dotenv').config()
const AWS = require('aws-sdk')
const ses = new AWS.SES({
    region: 'ap-southeast-2'
})
//Process the variables into an email and send it to ses.
const sendEmail = (name, message, senderEmail) => {
    const params = {
        Destination: {
            ToAddresses: [
                'abhishekcs96@gmail.com'
                ]
        },
        Message:{
            Body:{
                Text:{
                    Data: message,
                    Charset: 'UTF-8'
                }
            },
        Subject: {
            Data: name,
            Charset: 'UTF-8'
        }
        },
        Source: 'abhishekcs96@gmail.com',   // the source verified on ses.
        ReplyToAddresses: [senderEmail]      // identifies which address the email came from, to reply back to it.
    }
    // use the promise in order to fullfill the execution of the function with ses.
    // then return response object sent to index js async function to call context.done
    return ses.sendEmail(params).promise();
}

module.exports = sendEmail
