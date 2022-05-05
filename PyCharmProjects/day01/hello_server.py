from flask import Flask, render_template  # import the class 'Flask' from the module 'flask'
from markupsafe import escape


# create an object of class 'Flask'
app = Flask(__name__)


# map this method as a request-handler for a given url - http://localhost:8080/
@app.route('/')
def homepage():
    title = 'Hello, Infosys!'
    message = 'Created by Vinod, powered by Flask'
    friends = ['Shyam Sundar', 'Ramesh Iyer', 'Naveen Kumar', 'Harish Jagdeesh', 'Kishore Kumar']
    return render_template('hello.html', ttl=title, msg=message, friends=friends)
    # return """
    #     <h1>Hello, world!</h1>
    #     <hr />
    #     <p>Create by Vinod; Powered by Flask.</p>
    #     """


@app.route('/hello/<username>')  # http://localhost:8080/hello/Vinod
def hello_user(username):
    return f'<h1>Hello, {escape(username)}. How are you doing today?</h1>'


# start the server at a given port number
if __name__ == '__main__':
    app.run(port=8080, debug=True)
