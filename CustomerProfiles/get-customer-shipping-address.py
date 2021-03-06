from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

# Give merchant details
merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

# create get shipping address request
getShippingAddress = apicontractsv1.getCustomerShippingAddressRequest()
getShippingAddress.merchantAuthentication = merchantAuth
getShippingAddress.customerProfileId = "36152165"
getShippingAddress.customerAddressId = "36413544"

# Make the API call
getShippingAddressController = getCustomerShippingAddressController(getShippingAddress)
getShippingAddressController.execute()
response = getShippingAddressController.getresponse()

if response.messages.resultCode == "Ok":
    print "SUCCESS"
    print "The address is"
    print response.address.firstName +" " + response.address.lastName
    print response.address.address
    print response.address.city
    print response.address.state
    print response.address.zip
    print response.address.country
else:
    print "ERROR"
    print "Message code : %s " % response.messages.message[0].code
    print "Message text : %s " % response.messages.message[0].text
