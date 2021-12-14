from flask import Flask , render_template , request 
import urllib.request, json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

app = Flask(__name__)
url = "https://api.rootnet.in/covid19-in/stats/latest"
url_cases = "https://api.covid19api.com/country/india"

# this is for routing
@app.route("/" )
def index():
    if request.method == "GET":
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        datetime = dict["lastRefreshed"].split("T")
        time = datetime[1].split(".")[0]

        Confirmed = list()
        Date = list()

        response = urllib.request.urlopen(url_cases)
        data = response.read()
        dict2 = json.loads(data)
        for data in dict2:
            Confirmed.append(data["Confirmed"])
            var = data["Date"].split("T")
            Date.append(var[0])
        

        plt.plot(Date, Confirmed, label = "Total Cases")
        plt.legend()
        plt.savefig('static/image/pic.png')
        return render_template("index.html" , data = dict["data"] , date= datetime[0] , time = time)



# this run the Flask
if __name__ == "__main__":
    app.run(debug=True)