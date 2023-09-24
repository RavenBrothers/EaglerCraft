Getting Started:
-
Using Languages:
-
HTML -- Use Index.html
-
CSS -- Use  <link rel="stylesheet" href="styles.css">
-
JS -- Use <script type="text/javascript" src=""></script>
-
Python -- WE WILL BE USING FLASK 
-
pip install Flask [run in your command terminal if you haven't installed FLASK]
-
myapp/                  Use This Structure
├── templates/      
│   └── index.html
└── app.py
-
from flask import Flask, render_template

app = Flask(__name__)        In the app code your Flask app

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
-
python app.py          Start the app by using this code
-
By default, it will run on [http://127.0.0.1:5000/]
-
This is basic ... 
-
