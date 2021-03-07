import json

# Why? Json objects allow efficient and uniform transportation of data across the internet
### >>>> a json object is simply a python object that has been templated and put into a json file
### >>>> and this json file is what will be sent over the internet because json's are lightweight
### >>>> that are primarily text and can be served very quickly to many userbases and its a universal template
### >>>> you can throw a json file into about any application and it will now how to read the json file because all json files use this general syntax


#Before we make a json object lets make a regular python object and see the relation between the two

dictionary = {
    "key":"value" #weve been working with these dictionaries which are python objects and they utilize these Key/Value pairs
}

#We can make these more complex objects

#python dictionary sytax

dictionaryJoke = {
    "type": "success",
    "value": {
        "id": 493,
        "joke": "Chuck Norris can binary search unsorted data.",
        "categories": ["nerdy"]

    }
}

#copy/pasted from the newly created exampleObject.json file---
#compare the python object above and the json object below, 
#notice the few differences

#notice json does not do any variable declaration, its just a list of objects
#other than that it looks like everything is almost identical
#
#{
    #"type": "success",
    #"value": {
       # "id": 493,
       # "joke": "Chuck Norris can binary search unsorted data.",
       # "categories": [
        #    "nerdy"
      #  ]
   # }
#}

#an object in json is going to be almost identical except its going to be in a json file

#json objecrts must be in json files.
#we are going to use this python file to create this json file and write this python object into it

#lets go ahead a use a little bit of pythons built in libraries

#start with the json package (import json)^^^^

#to write a new file I'm going to say....

with open('exampleObject.json', 'w') as outfile: #in order to interact with it we will label it as outfile
#we are writing the file so I amgoing to give it that keyword 'w' == 'write'
#the last thing we are going to do is use the json package we just installed, and to write a new json object we will use the dump method
    json.dump(dictionaryJoke, outfile, indent=4) #<<<<<<<<  indent=4 is just a styling thing
#the idea is that we are going to "dump" what ever object is currently written in python, and turn it into json
#we are going to dump the (dictionaryJoke) object into the (exampleObject.json)file. We are going to add a couple


#weve created json objects
#we know what they look like 
#and we know they are used to transporting data efficiently from a route

#lets take the json and put it in a route and see what happens
#go to server (mainfile.py)file and write a route that would return this json object as a result (mainfile.py - line 103)