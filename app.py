from flask import *
app = Flask(__name__)
import requests
import json

url = "https://ai-quote3.p.rapidapi.com/ai-quotes/"

headers = {
	"X-RapidAPI-Key": "13a3fdc433mshc472900b88d594cp11dce7jsnadce2b996b30",
	"X-RapidAPI-Host": "ai-quote3.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

# print(response.text)

a = response.text
b = json.loads(a)

# print(type(b))
# print(response.text)
# print(b)

@app.route('/')
def index():
    data = b
    return render_template('index.html', data=b)

if __name__ == '__main__':
    app.run(debug=True)