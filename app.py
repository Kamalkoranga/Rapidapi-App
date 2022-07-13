from flask import *
app = Flask(__name__)
import requests, random
import json

sno = random.randint(0,9)
print(sno)

url = f"https://ai-quote3.p.rapidapi.com/ai-quotes/{sno}"

headers = {
	"X-RapidAPI-Key": "13a3fdc433mshc472900b88d594cp11dce7jsnadce2b996b30",
	"X-RapidAPI-Host": "ai-quote3.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

a = response.text
b = json.loads(a)

print(type(b))
print(response.text)
print(b)

@app.route('/')
def index():
    data = b
    return render_template('index.html', data=b)

if __name__ == '__main__':
    app.run(debug=True)