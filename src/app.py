from flask import Flask

app = Flask(__name__)
app.debug = True

from routes.index import *

if __name__ == '__main__':
    app.run()