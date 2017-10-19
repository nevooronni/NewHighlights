from flask import Flask

#initializing the applictaion 
app = Flask(__name__,instance_relative_config = True)#when the instance is created we want to access the instance folder

#setting up configuration 
app.config.from_object(DevConfig)#import the devconfig sublass to use in our app  and use the app.config.from_object
app.config.from_pyfile('config.py')#connects to config.py all all of its contencts appended to app.config

from app import news