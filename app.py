from flask import Flask , render_template , request 
import urllib.request, json
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
url = "https://api.rootnet.in/covid19-in/stats/latest"

# this is for routing
@app.route("/" )
def index():
    if request.method == "GET":
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        datetime = dict["lastRefreshed"].split("T")
        time = datetime[1].split(".")[0]
        states = list()
        cases = list()
        for state in dict["data"]["regional"]:
            states.append(state["loc"])
            cases.append(state["confirmedCasesIndian"])
        
        x = states
        y = cases
        plt.barh(x, y)
        plt.savefig('static/image/pic.png')
        return render_template("index.html" , data = dict["data"] , date= datetime[0] , time = time)



# this run the Flask
if __name__ == "__main__":
    app.run(debug=True)