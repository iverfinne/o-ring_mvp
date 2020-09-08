from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

import routes

if __name__ == "__main__":
    # Only for debugging while developing
    # app.run(host='0.0.0.0', debug=True, port=80)
    app.run(host='0.0.0.0', debug=True, port=6000)