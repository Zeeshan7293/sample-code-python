from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

creditCard = apicontractsv1.creditCardType()
creditCard.cardNumber = "4111111111111111"
creditCard.expirationDate = "2020-12"
creditCard.cryptogram = "EjRWeJASNFZ4kBI0VniQEjRWeJA="

payment = apicontractsv1.paymentType()
payment.creditCard = creditCard

transactionrequest = apicontractsv1.transactionRequestType()
transactionrequest.transactionType = "authCaptureTransaction"
transactionrequest.amount = Decimal ('1.5')
transactionrequest.payment = payment

createtransactionrequest = apicontractsv1.createTransactionRequest()
createtransactionrequest.merchantAuthentication = merchantAuth
createtransactionrequest.refId = "MerchantID-0001"
createtransactionrequest.transactionRequest = transactionrequest

createtransactioncontroller = createTransactionController(createtransactionrequest)
createtransactioncontroller.execute()

response = createtransactioncontroller.getresponse()

if (response.messages.resultCode=="Ok"):
	print "SUCCESS"
	print "Message Code : %s" % response.messages.message[0].code
	print "Message text : %s" % response.messages.message[0].text
	print "Transaction ID : %s" % response.transactionResponse.transId
else:
	print "ERROR"
	print "Message Code : %s" % response.messages.message[0].code
	print "Message text : %s" % response.messages.message[0].text
