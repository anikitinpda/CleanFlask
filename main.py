from flask import *
from uptime import *

app = Flask(__name__)

@app.route("/")
def ello():
      piuptime = uptime()
      return render_template('index.html', piuptime=piuptime)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
