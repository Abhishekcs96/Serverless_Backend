
const emailsending = require('./sendEmail')
const index = require('./index')
const expectExport = require('expect')
const { expect } = require('@jest/globals')

const RealResponse = 'Email sent'
test('Email sent test', () => { 
   return index.handler({
    "name" : "TestEvent",
    "email" : "testing@email.com",
    "message" : "This is a test email."
}, 0).then(data =>{
    expect(data).toBe('Email sent')
} )
})