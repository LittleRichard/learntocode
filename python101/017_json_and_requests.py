import pprint
import random
import requests
# handles pretty much all the bits & bytes for you,
# including URL encoding of QPs!!!

# let's try using query params
SEARCH_URL = 'http://www.google.com/search'
query_params = {
    'q': 'coding is fun'
}

response = requests.get(SEARCH_URL, params=query_params)
# notice how requests.get() formatted the URL for us?
print(f'response URL {response.url}')
print(f'response code {response.status_code}')

# there isn't any JSON data in this response, so we'll
# look at the 'text' field... but it's an HTML file
# so let's save it somewhere
with open('data/google_example.html', 'w') as fh:
    fh.write(response.text)

# open this file using a browser!

# documentation for API is at:
# https://dog.ceo/dog-api/documentation/
DOG_API_BASE_URL = 'https://dog.ceo/api/'

# make a request to list all breeds
ALL_BREEDS_PATH = DOG_API_BASE_URL + 'breeds/list/all'

# issue a GET request
response = requests.get(ALL_BREEDS_PATH)
# there are lots of response codes...
# 2XX: OK
# 4XX: You did something wrong
# 5xx: The server did something wrong
print(f'response code {response.status_code}')

print("""
IMPORTANT PRO TIP: Your web browser obscures the fact
that it's doing exactly the same thing that we are here!

As you use URLs for various things, try using the
'developer tools' available in firefox and chrome
to get a sense of what is happening; put them into
a browser and see what happens!  If you get back:
- a formatted web page: the website returned a bunch
  of text that happens to be well-formatted HTML and
  your browser knows how to 'run HTML code' to display
  it to you
- a bunch of raw text: could be anything, but is likely
  to be JSON-formatted data; this signifies that the URL
  is for some kind of API
- image/audio/video: raw binary data formatted as JPG,
  GIF, MOV, etc, which the browser can 'run' to show it
  as you're used to seeing it.

In all cases, it's the same process: you request some info
from a URL and it gives it back; it's what you do AFTER
you receive it that is important.
""")

# the return data from APIs will not be consistent,
# but in this case the API is returning JSON to us.
# JSON is a format for representing data,
# and handles complex nested data structures

# converts the JSON to a dict for us
resp_data_from_json = response.json()
print(f'response JSON {response.json()}')
print('Pretty printed JSON:')
pprint.pprint(resp_data_from_json)

print("""
This JSON is a dictionary containing another
dictionary mapping dog types to lists of sub-types.
""")

# print all terrier types. why this structure?
# we don't get to choose, we're just consuming the
# API's results...
retrievers = resp_data_from_json['message']['retriever']
print(f'retrievers: {retrievers}')

print(f"""
Some APIs rely on transmitting a 'payload' instead
of or in addition to query parameters. You can send
this data like:

# in a GET
requests.get(SOME_URL, data=my_payload_dict)
# in a POST
requests.post(SOME_URL, data=my_payload_dict)

POST requests typically involve an action
that will result in persisting some data, which
is almost never going to be exposed in a public API
and thus is hard to find simple examples for.
""")
