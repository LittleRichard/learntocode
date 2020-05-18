## The Internet

Most of the time you'll be interacting with a 'client-server' model, where a client (like you in your web browser) makes a request to a server, which is running at an IP address listening for web requests.  It looks something like the following pseudocode:
```
# this is a classic use case for an infinite loop!
while True:
    request = get_request()
    if request:
        process_request(request)
```

### Client side
A client can make a request to the server for data, which the server will either recognize, handle, and respond to...  Or the request won't make sense to the server and it will respond with an error.  You've all done this using URLs; a URL is composed of several pieces, and we'll use this one 
https://www.google.com/search?q=coding+is+fun&dummy=not_used

**https://**
Indicates that data will be transmitted using HyperText Transfer Protocol Secure 
 - Protocols and the layers of the internet are BIG TIME bits & bytes... all we need to know is that there are different protocols and http is the one you'll interact with almost exclusively.
 - The 's' for Secure means that it is encrypted end-to-end; this can still be broken by a 'man in the middle' attack watching the handshake that sets up the encryption happen between client and server.

**www.google.com**
This is a hostname, which is translated to an IP by a DNS server.  Bits & Bytes abound here as well, but this is kind of like the locker problem with mutable variables.  A hostname is a lot like a label, which maps to a physical IP address, and DNS is the lookup that means you as a person don't have to remember the IP.  It also means that servers can rotate IPs as long as the DNS is updated to match.

**/search**
This is the path, which describes a specific resource that this server will know how to process.  In this case, we're asking the server to access its `search` capability and return a web page with search results.  You can imagine how `/map` would do the same thing but with a map.

**?q=coding+is+fun&dummy=not_used**
The `?`means that the following text will describe 'query parameters'., where each parameter is separated by an `&`  Query parameters resemble python dictionaries, in the sense that they have keys (the parameter name) and values (parameter values).  URLs can only contain certain characters (notably, not spaces), so URLs are hard to decipher sometime because they are encoded.  The `+` character is how `google.com/search` expects spaces to be encoded!  These query parameters in python dictionary form would look like:
```
query_params = {
   'q': 'coding is fun',
   'dummy': 'not used'
}
```
`google.com/search` expects a QP called `q`, which contains the string you'd like to search.  I've also included a QP called `dummy` that the server is not expecting, but completely ignores (as best as I can tell); some servers will tell you that your URL is invalid if it contains bonus QPs.

### Server side
The server receives the request and parses it to know which could should be executed based on the `path`.   So the `/search` path might lead to a function that does this (pseudocode):
```
import google_search  # the code worth billions
import urllib

def handle_search(q):
    # first remove all the encoding that the browser added
    # to make the URL syntactically valid
    query_params = urllib.parse.parse_qs(q)
    search_query = query_params['q']
    
    return google_search.search_string(search_query)
```
The server creates a payload and sends it back, where the browser (or code you're running in the browser that generated a request) knows how to render it and voila, you see your results.

### More complex requests
This example was of a `GET` request, but there are other types!  `PATCH` is for sending an update, and `POST` is for sending new information (and is also frequently used to trigger a function on a server).  `PATCH` and `POST` use 'payloads' in addition to QPs, more on that next.

### Authentication
Not all APIs will respond to your requests because they're protected,
either because they don't want to deal with the volume of public requests
or because they have data to protect. Common authentication methods:
 - API key: outside of code you'll request an API key, which you'll need
 to include in your request or the server will return an error code indicating that you are Forbidden or Not Authorized.
 - Token based access: similar to an API key, but you have to request a new token periodically using a username/password.  This is essentially how you log into and use websites; your browser handles the token for you so you don't need to include username/password all the time.