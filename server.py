from flask import Flask

app = Flask(__name__)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC123"

# So any undefined variables in Jinja will raise an error
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    DebugToolbarExtension(app)
    app.run()
