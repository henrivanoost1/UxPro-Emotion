import os 
import json
from flask import json
from flask import Flask, render_template


app = Flask(__name__)

# @app.route("/")
def showpage():
    lst = os.listdir('./videos')
    item_list = []
    for item in lst:
        item_list.append(item)
        send = json.dumps(item_list)
        # user = {"FN": "Thibault", "LN":"D'haese"}

    return render_template("index.html", send = send)


# if __name__ == "__main__":
#     app.run()
