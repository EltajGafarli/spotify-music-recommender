from flask import Flask


app = Flask('__main__',template_folder='app/templates')


from app import routes
