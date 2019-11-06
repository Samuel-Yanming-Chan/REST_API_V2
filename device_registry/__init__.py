import markdown
import os

from flask import Flask

#Create an instance of Flask
app = Flask(__name__)

@app.route("/")
def index():
    # Present the documentation

    # Open readme
    with open(os.path.dirname(app.root_path) +'/README.md','r') as markdown_file:

        #read content
        content = markdown_file.read()

        #Convert to HTML
        return markdown.markdown(content)
