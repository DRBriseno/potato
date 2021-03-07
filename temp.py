# Objective = create servers that fulfill request

# Step 1 = import the flask library for usage
# HOW = use simple python syntax to say
# from flask library import flask object WHICH LOOKS LIKE THE CODE BELOW

from flask import Flask
 
 # how do we know it actually exists and is available?

 # we are going to install python 3 by typing pip3 install in terminal
 # now that we are done with that and flask is installed we are going to the next step
 # create an instance of the flask server

# we are going to do that by using the FLask() method, this is going to create that flask object
# but we dont want to create a server without anything assigned to it so we are going to assign
# it to a variable we can reference somewhere down the line
# we are going to call it app, sometimes it gets called server WE ARE GOING TO DO SO BY THE COMMAND BELOW

# app = Flask()
# inside of this flask object we want to pass the root directory
# as the root directory within 'main.py'
# WHAT IM REALLY DOING: I'm creating an instance of a flask server with this instance of a flask object
# which I've imported from the flask library, I'm assigning it to this variable called app,and I want to 
# use a root directory inside of it called name
app = Flask(__name__)
# nect step create some routes
# reference app (server) but befor we do that we use a decorator @
# to utilize a route within the flask object it's as simple as 
# @app.route
# DecoratorAppDotRoute and then im going to pass it a single argument 
# and it is going to be the location of the route in the server
# @app.route('/')
# this is going to be the default route that the request gets sent to
# so we have a route here but we want it to actually do something ,
# we want it to return some valueclear

# so we are going to create a function
@app.route('/')
def displayHomepage():
    return "<h1> Welcome to your first website!!! You did it, Rose! </h1>"
# we created a route and three lines of code
# lets create a second route
@app.route('/route1')
def route1Info():
    return "<h3> Congrats! You created route1! </h3>"
# finally our last step is to make sure the server an turn on and listen for requests
# turn server on for serving
# a good practice to leverage is that we always want to have a main loop
# a main loop is going to look like
# the main loop is alawys going to look something like this
# if __name__ == "__main__":
#    app.run
# we are going to run it
# but first we need to add perimeters, starting with debug so if there is ever an error
#we can see it, and lets tell it to listen on port 3000
if __name__ == "__main__":
     app.run(debug=True, port=3000)

# if the name of the file getting run is equal to main we will run

# we have all the code we need for a working server, before we run it, lets just test the server
# do this by typing python3 main.py in the teminal


