### First off
- If you want to be able to program, do the homework, examples, practice, 
practice, practice. Watching baseball will teach you how to play, but if 
you've never swung a bat you probably suck at it. Many people
enjoy understanding and watching things they're bad at, and that's cool
too. Just match your expectations to your effort.
- Everyone learns their own way: visuals, examples,
office hours, anything is possible, but you have to let your teacher know!

#### 1955 - FORTRAN gave programmers conditional logic (if/else) and math.  
Still used for weather forecasting today, extremely fast at math.

#### 1972 - C gave programmers a layer of abstraction over bits/bytes.  
- Pre-compiled, blazing fast, but still requires knowledge of how 
your program is executed on the processor and consumes RAM
- Programmer must manage memory, uses 'pointers' to memory; kind of
like calling someone by their SSN instead of their name, and equally 
dangerous.

#### 1991 - Python, a high-level dynamically-typed language
- has its own syntax that leverages the good parts of C, but 
abstracts the code from the way it's executed.  
- Reads like english, and is very flexible.
- "We're all adults here", philosophy that the language isn't 
responsible for protecting programmers from themselves.

#### Today - Python libraries exist to do EVERYTHING.  
Making an application in python is much more about figuring out how 
to glue things together than anything else, so if you get really good
at glue you can do some SERIOUSLY powerful stuff.
For example, do you know to send a text from a computer? I don't either,
but I do know how to install the 'Twilio' python package.
```
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+15017122661',
         to='+15558675310'
     )
```
A few more interesting examples:
- complex data analysis
- home automation server
- ruin internet polls
- use any API

#### A little speech
Programming is the art of learning how tools are designed to be used. This 
class will show you the foundational tools in your toolbox, and examples 
of using them.

Development is the art of learning how to apply all of the tools at your
disposal to fight a problem in the most straightforward way.

Engineering is the art of making something work in the real world, over
time, with as little excitement as possible.

You can learn programming, development takes practice, and if you figure out
engineering please let me know. 
