#Why? We need to be able to collect data from users.
#1.Utilize route variables to get data from the url
#2.Utilize form data to collect large swaths of information/data at once
#3.Seperate python from the html and make it scalable
#4. We want a general look to our websites that reuse components when possible.

#import flask library for usage.
from flask import Flask, request, render_template
import json

#create an instance of a flask server
#as the root directory within mainfile.py
app = Flask(__name__)

#create a route
@app.route('/')
def displayHomepage():
    return render_template('index.html')


#create a route
#@app.route('/route1')
#def route1Info():
    #return "<h3> Congrats on creating route 1! </h3>"

#create a route   --- < > denotes a route variable
#@app.route('/profile/<users_name>')
#def profile(users_name):
    #return "<h2> Hello" + users_name + "!</h2>"

#@app.route('/date/<month>/<day>/<year>')
#def displayGivenDate(month,day,year):
    #return f"{month}/{day}/{year}"


#Creating a <form>
 #/form action = "/result" method="GET">

#formData= f"""
    #<form action = "/results" method="GET">
        #What's your favorite pizza flavor?"
        #<input type="text" name="pizza_flavor">
        #<br>
        #What's your favorite crust flavor?
        #<input type="text" name="crust">
        #<input type="submit" value="submit pizza">
        #<br>
    #</form>
    #"""

@app.route('/formExample')
def firstForm():
    return render_template('form.html')


@app.route('/results', method=['GET'])
def simple_pizza_results():

# a context object contains all the necessary form data the template
    context = {
        'pizza_flavor': request.args.get("pizza_flavor"),
        'crust': request.args.get("crust")
        'individual_toppings': ['mushrooms', 'olives', 'garlic']
    }
    #pizza_flavor = request.args.get("pizza_flavor")
    #crust = request.args.get("crust")
    return render_template('confirmation_page.html', **context)


    #^^^^^^^^^^^^^^
    ## a Python route that returns a rendered template
    #example below:

#def submit_pizza():
    #context = {
        #'users_email': request.args.get('email'),
        #'users_phone': request.args.get('phone'),
        #'crust_type': request.args.get('crust'),
        #'pizza_size': request.args.get('size')
    #}
		
		# this code returns a template of HTML instead of plain text
    #return render_template('submission_page.html', **context)

    #------becomes--------
#Fig 1 - a previous example from the Templates lesson that passes in a context object
#Since we pass the context object to render_template() using the **kwargs syntax, we could also pass in a series of key-value pairs defined as parameters as in Fig 2.
#This example gives exactly the same result as the previous example.

#--------becomes-----------


    #def submit_pizza():
    #return render_template('submission_page.html',
        #users_email=request.args.get('email'),
        #users_phone=request.args.get('phone'),
        #crust_type=request.args.get('crust'),
        #pizza_size=request.args.get('size'))


with open('exampleObject.json') as example_obj_file:
    print("raw file printed = ", example_obj_file)
    jsonData = json.load(example_obj_file) #<<<< load is the inverse of dump (it takes a json object and turns it into a python object) that we can interact with normally
    print("just the JSON data printed = ", jsonData)

@app.route('/jsonExample', methods=[GET])
def jsonRoute():
    return jsonData


#turn the server on for serving
if __name__ == "__main__":
    app.run(debug= True, port= 3000)

