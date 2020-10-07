"""
Simple demonstrations on how to use Python's "requests" library.

Studies based on this tutorial: https://realpython.com/python-requests/

requests library Docs: https://requests.readthedocs.io/en/master/

@author hedersantos
"""

import requests
from getpass import getpass
from requests.exceptions import Timeout
from requests.exceptions import HTTPError


"""----------------------------------------------------------------------------
the GET method
----------------------------------------------------------------------------"""
response = requests.get('https://api.github.com')

# get() returns an instance of Response Class
print('"requests.get()" returns an instance of:',type(response))

print('"Response.status_code" attribute contains:',response.status_code)

"""----------------------------------------------------------------------------
PAYLOAD
----------------------------------------------------------------------------"""

# get Response's payload in formats like bytes ...
print('\n payload as BYTES: \n\n',response.content)

# ... string (notice how encoding is defined first)
response.encoding = 'utf-8'

print('\n payload as STRING: \n\n',response.text)

# ... JSON (notice it's a method, not an attribute)
payloadDict = response.json()

# explore payload dictionary keys
print('\n PAYLOAD dictionary has the following keys: \n')

for key in payloadDict.keys():
    print(key)

print('\n payload as JSON: \n\n',payloadDict)

# set target element as string
targetElement = 'current_user_url'

print(f"\n access payload '{targetElement}' element from dictionary:", payloadDict[targetElement])

print('\n "Response.json()" returns an object of type:',type(payloadDict))

"""----------------------------------------------------------------------------
HEADERS

Keep in mind Response's headers is of type "CaseInsensitiveDict"
----------------------------------------------------------------------------"""

# get Reponse's "headers" dictionary
headersDict = response.headers

# use Response's headers attribute to access request metadata
print("\n Response's 'headers' attribute contains: \n\n",headersDict)

print('\n "headers" is of type',type(headersDict))

# access headers' "Content-Type" contents
print("\n headers' 'content-type' contains:",headersDict['content-type'])

"""----------------------------------------------------------------------------
QUERY STRING PARAMETERS
----------------------------------------------------------------------------"""

# use GitHub's Search API to look for "requests" repo
# GET has a "params" parameter which is a dictionary with with it's possible to
# customize your HTTP requests through query string parameters.
response = requests.get(
     'https://api.github.com/search/repositories'
    ,params={'q':'requests+language:python'}
)

json_response = response.json()

for key in json_response.keys():
    print(key)

print(f"\n GitHub's Search API retuned {json_response['total_count']} results.")

# return first element within "items" key (items is a list of dictionaries)
repository = json_response['items'][0]

print(f"\n REPOSITORY name: {repository['name']}.")
print(f"\n REPOSITORY description: {repository['description']}.")

"""----------------------------------------------------------------------------
REQUEST HEADERS
----------------------------------------------------------------------------"""

# use GET's "headers" parameter for headers customization: "Accept" informs the
# server what content types our application can handle.
response = requests.get(
     'https://api.github.com/search/repositories'
    ,params={'q':'requests+language:python'}
    ,headers={'Accept':'application/vnd.github.v3.text-match+json'}
)

json_response = response.json()

repository = json_response['items'][0]

print(f"Text Matches: {repository['text_matches']}")

"""----------------------------------------------------------------------------
MESSAGE BODY
----------------------------------------------------------------------------"""

# use Kenneth Reitz's service to test different HTTP methods and their responses
httpService = 'https://httpbin.org'

# POST's "data" parameter either receives a Dictionary or a List of Tuples
response = requests.post(httpService + '/post',data={'key':'value'})

print(response)

# use "json" parameter to send JSON objects
response = requests.post(httpService + '/post',json={'myKey':'myValue'})

# parse Response as JSON. KEEP IN MIND keys here are CASE SENSITIVE!
json_response = response.json()

# print out the data we sent to the server
print(f"\n JSON sent was: {json_response['data']}")

print(f"\n Content-Type is: {json_response['headers']['Content-Type']}")

print(f"\n POST Response.json() is of type {type(json_response)}")

"""----------------------------------------------------------------------------
REQUEST PREPARATION AND INSPECTION

    Python's "requests" library prepares your HTTP request before sending it to 
it's destination server. This preparation includes headers validation and JSON 
content serialization.
----------------------------------------------------------------------------"""

# use Response's "request" attribute to inspect your request after preparation
print(f"\n PREPARED request attributes are shown below:")

print(f"\n 'headers': {response.request.headers['Content-Type']}")

print(f"\n 'url': {response.request.url}")

print(f"\n 'body': {response.request.body}")

"""----------------------------------------------------------------------------
AUTHENTICATION

    "requests" methods provide an "auth" parameter through which it's possible
to authenticate on servers who are not public.

    Notice a Token could be added to request's headers through 'X-TokenAuth'.
----------------------------------------------------------------------------"""

# "auth" receives a Tuple having Username and Password. "getpass" is used here
# to prompt for passwords at runtime.
response = requests.get(
     'https://api.github.com/user'
    ,auth=('username', getpass())
)

json_response = response.json()

print(json_response)

# "requests" verifies SSL Certificates by default. Nevertheless it's possible 
# to disable such behaviour using a method's "verify" parameter.
print(f'\n ISSUING request without SSL Certificate verification...')

response = requests.get('https://api.github.com', verify=False)

print(response)

"""----------------------------------------------------------------------------
PERFORMANCE
----------------------------------------------------------------------------"""

# a method's "timeout" parameter determines how long it should wait for a server
# response. Below there's a 1 second timeout set
print(f"\n 1 SECOND-timeout request response: {requests.get('https://api.github.com', timeout=1.0)}")

# it's also possible to determine both "connection" and "read" timeouts by passing
# a Tuple to "timeout" (NOTICE it handles both Integers and Floats as input).
print(f"\n 2 SECONDS Connect, 5 SECONDS Read: {requests.get('https://api.github.com', timeout=(2,5.0))}")

# Timeout errors handling
print(f"\n TIMEOUT error handling section:")

try:
    # both connection and read operations must happen in 1 second at most
    response = requests.get('https://api.github.com', timeout=(1,1))
except Timeout:
    print(f'\n TIME. IS. OUT! =(')
else:
    print(f"\n SUCCESS! Response is: {response}")

"""----------------------------------------------------------------------------
THE SESSION OBJECT

    Requests are abstracted through usage of a Session Class. Use this Class
to fine tune your requests by, for example, using the same credentials for
different requests, reusing available connections instead of creating new ones,
etc.
----------------------------------------------------------------------------"""

print(f"\n USING Session to fine tune requests")

# make sure resources are released after usage by using context management
with requests.Session() as session:

    # set credentials for entire Session
    session.auth = ('username', getpass())

    # invoke GET method from Session instead of "requests"
    response = session.get('https://api.github.com/user')

print(f"\n headers: {response.headers}.")
print(f"\n Response.json(): {response.json()}.")

# Retries and TransportAdapters

print(f"\n RETRIES section")

github_adapter = requests.adapters.HTTPAdapter(max_retries=3)

# instantiate Session() Class
session = requests.Session()

# mount HTTPAdapter onto Session instance
session.mount('https://api.github.com', github_adapter)

try:
    # send request to github server
    print(session.get('https://api.github.com'))
except requests.exceptions.ConnectionError as ce:
    print(ce)





